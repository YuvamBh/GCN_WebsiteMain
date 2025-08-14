"""
Enhanced Features for GCN Website
Additional utilities and functionality for the Global Career Network website
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import logging

# Airtable integration
try:
    from pyairtable import Api, Base, Table
    AIRTABLE_AVAILABLE = True
except ImportError:
    AIRTABLE_AVAILABLE = False
    logging.warning("pyairtable not available. Feedback form will not work.")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GCNAnalytics:
    """Analytics tracking for GCN website interactions"""
    
    def __init__(self, data_file: str = "analytics_data.json"):
        self.data_file = data_file
        self.analytics_data = self._load_analytics()
    
    def _load_analytics(self) -> Dict:
        """Load existing analytics data from file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error loading analytics data: {e}")
        
        return {
            "page_views": {},
            "resource_clicks": {},
            "form_submissions": {},
            "events": []
        }
    
    def _save_analytics(self):
        """Save analytics data to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.analytics_data, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving analytics data: {e}")
    
    def track_page_view(self, page_name: str):
        """Track page view"""
        if page_name not in self.analytics_data["page_views"]:
            self.analytics_data["page_views"][page_name] = 0
        self.analytics_data["page_views"][page_name] += 1
        self._save_analytics()
        logger.info(f"Page view tracked: {page_name}")
    
    def track_resource_click(self, resource_name: str):
        """Track resource link click"""
        if resource_name not in self.analytics_data["resource_clicks"]:
            self.analytics_data["resource_clicks"][resource_name] = 0
        self.analytics_data["resource_clicks"][resource_name] += 1
        self._save_analytics()
        logger.info(f"Resource click tracked: {resource_name}")
    
    def track_form_submission(self, form_type: str, data: Dict):
        """Track form submission"""
        timestamp = datetime.now().isoformat()
        submission = {
            "timestamp": timestamp,
            "form_type": form_type,
            "data": data
        }
        self.analytics_data["events"].append(submission)
        self._save_analytics()
        logger.info(f"Form submission tracked: {form_type}")
    
    def get_analytics_summary(self) -> Dict:
        """Get analytics summary"""
        total_page_views = sum(self.analytics_data["page_views"].values())
        total_resource_clicks = sum(self.analytics_data["resource_clicks"].values())
        total_form_submissions = len([e for e in self.analytics_data["events"] if e.get("form_type")])
        
        return {
            "total_page_views": total_page_views,
            "total_resource_clicks": total_resource_clicks,
            "total_form_submissions": total_form_submissions,
            "top_pages": sorted(self.analytics_data["page_views"].items(), key=lambda x: x[1], reverse=True)[:5],
            "top_resources": sorted(self.analytics_data["resource_clicks"].items(), key=lambda x: x[1], reverse=True)[:5]
        }

class GCNFormProcessor:
    """Process and validate form submissions"""
    
    def __init__(self):
        self.required_fields = {
            "join": ["firstName", "lastName", "email", "major", "graduationYear"],
            "contact": ["name", "email", "message"],
            "feedback": ["name", "feedbackType", "message"]  # Name required, email optional
        }
        
        # Airtable configuration
        self.airtable_api_key = os.getenv('AIRTABLE_API_KEY') or os.getenv('AIRTABLE_PERSONAL_ACCESS_TOKEN')
        self.airtable_base_id = os.getenv('AIRTABLE_BASE_ID')
        self.airtable_table_name = os.getenv('AIRTABLE_TABLE_NAME', 'Feedback')
        
        if AIRTABLE_AVAILABLE and self.airtable_api_key and self.airtable_base_id:
            try:
                self.airtable_table = Table(self.airtable_api_key, self.airtable_base_id, self.airtable_table_name)
                self.airtable_available = True
                logger.info("Airtable connection established successfully")
            except Exception as e:
                logger.error(f"Failed to connect to Airtable: {e}")
                self.airtable_available = False
        else:
            self.airtable_available = False
            logger.warning("Airtable not configured. Set AIRTABLE_API_KEY and AIRTABLE_BASE_ID environment variables.")
    
    def validate_form_data(self, form_type: str, data: Dict) -> Dict:
        """Validate form data and return validation result"""
        errors = []
        
        if form_type not in self.required_fields:
            return {"valid": False, "errors": ["Invalid form type"]}
        
        required = self.required_fields[form_type]
        
        for field in required:
            if field not in data or not data[field].strip():
                errors.append(f"{field} is required")
        
        # Email validation
        if "email" in data and data["email"]:
            if not self._is_valid_email(data["email"]):
                errors.append("Invalid email format")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors
        }
    
    def _is_valid_email(self, email: str) -> bool:
        """Basic email validation"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def process_join_form(self, data: Dict) -> Dict:
        """Process join form data"""
        validation = self.validate_form_data("join", data)
        
        if not validation["valid"]:
            return validation
        
        # Process the form data (could save to database, send email, etc.)
        processed_data = {
            "firstName": data["firstName"].strip(),
            "lastName": data["lastName"].strip(),
            "email": data["email"].strip().lower(),
            "major": data["major"].strip(),
            "graduationYear": data["graduationYear"],
            "interests": data.get("interests", "").strip(),
            "submitted_at": datetime.now().isoformat()
        }
        
        return {
            "valid": True,
            "data": processed_data,
            "message": "Form submitted successfully!"
        }
    
    def process_feedback_form(self, data: Dict) -> Dict:
        """Process feedback form data and store in Airtable"""
        validation = self.validate_form_data("feedback", data)
        
        if not validation["valid"]:
            return validation
        
        # Process the form data to match Airtable column names
        processed_data = {
            "Type": data["feedbackType"],
            "Content": data["message"].strip()
        }
        
        # Add name (required)
        processed_data["Name"] = data["name"].strip()
        

        
        # Add email if provided (optional)
        if data.get("email") and data["email"].strip():
            processed_data["Email"] = data["email"].strip().lower()
        
        # Store in Airtable if available
        if self.airtable_available:
            try:
                record = self.airtable_table.create(processed_data)
                logger.info(f"Feedback stored in Airtable: {record['id']}")
                return {
                    "valid": True,
                    "data": processed_data,
                    "message": "Thank you for your feedback! It has been submitted successfully.",
                    "airtable_id": record['id']
                }
            except Exception as e:
                logger.error(f"Error storing feedback in Airtable: {e}")
                return {
                    "valid": False,
                    "errors": ["Failed to store feedback. Please try again later."]
                }
        else:
            # Fallback: store locally if Airtable is not available
            logger.warning("Airtable not available. Storing feedback locally.")
            return {
                "valid": True,
                "data": processed_data,
                "message": "Thank you for your feedback! It has been submitted successfully.",
                "stored_locally": True
            }

class GCNContentManager:
    """Manage dynamic content for the website"""
    
    def __init__(self):
        self.content_file = "content_data.json"
        self.content = self._load_content()
    
    def _load_content(self) -> Dict:
        """Load content data"""
        try:
            if os.path.exists(self.content_file):
                with open(self.content_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error loading content: {e}")
        
        return {
            "upcoming_events": [],
            "success_stories": [],
            "announcements": [],
            "featured_resources": []
        }
    
    def _save_content(self):
        """Save content data"""
        try:
            with open(self.content_file, 'w') as f:
                json.dump(self.content, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving content: {e}")
    
    def add_event(self, event_data: Dict):
        """Add new event"""
        event_data["id"] = len(self.content["upcoming_events"]) + 1
        event_data["created_at"] = datetime.now().isoformat()
        self.content["upcoming_events"].append(event_data)
        self._save_content()
        logger.info(f"Event added: {event_data.get('title', 'Untitled')}")
    
    def add_success_story(self, story_data: Dict):
        """Add new success story"""
        story_data["id"] = len(self.content["success_stories"]) + 1
        story_data["created_at"] = datetime.now().isoformat()
        self.content["success_stories"].append(story_data)
        self._save_content()
        logger.info(f"Success story added: {story_data.get('name', 'Anonymous')}")
    
    def get_upcoming_events(self, limit: int = 5) -> List[Dict]:
        """Get upcoming events"""
        return self.content["upcoming_events"][:limit]
    
    def get_success_stories(self, limit: int = 3) -> List[Dict]:
        """Get success stories"""
        return self.content["success_stories"][:limit]
    
    def get_announcements(self) -> List[Dict]:
        """Get announcements"""
        return self.content["announcements"]

class GCNUtilities:
    """Utility functions for GCN website"""
    
    @staticmethod
    def format_date(date_string: str) -> str:
        """Format date string for display"""
        try:
            date_obj = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            return date_obj.strftime("%B %d, %Y")
        except:
            return date_string
    
    @staticmethod
    def truncate_text(text: str, max_length: int = 100) -> str:
        """Truncate text to specified length"""
        if len(text) <= max_length:
            return text
        return text[:max_length].rsplit(' ', 1)[0] + "..."
    
    @staticmethod
    def generate_slug(text: str) -> str:
        """Generate URL-friendly slug from text"""
        import re
        slug = re.sub(r'[^\w\s-]', '', text.lower())
        slug = re.sub(r'[-\s]+', '-', slug)
        return slug.strip('-')
    
    @staticmethod
    def validate_image_file(filename: str) -> bool:
        """Validate image file extension"""
        allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}
        return any(filename.lower().endswith(ext) for ext in allowed_extensions)

# Initialize global instances
analytics = GCNAnalytics()
form_processor = GCNFormProcessor()
content_manager = GCNContentManager()
utilities = GCNUtilities()

def get_website_stats() -> Dict:
    """Get website statistics"""
    return analytics.get_analytics_summary()

def process_contact_form(form_data: Dict) -> Dict:
    """Process contact form submission"""
    return form_processor.validate_form_data("contact", form_data)

 