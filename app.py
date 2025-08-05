from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
import os
from enhanced_features import analytics, form_processor, content_manager, utilities

app = Flask(__name__)
app.secret_key = 'gcn_secret_key_2024'

# Routes
@app.route('/')
def home():
    analytics.track_page_view('home')
    return render_template('index.html')

@app.route('/team')
def team():
    analytics.track_page_view('team')
    return render_template('team.html')

@app.route('/events')
def events():
    analytics.track_page_view('events')
    return render_template('events.html')

@app.route('/events/upcoming')
def upcoming_events():
    analytics.track_page_view('upcoming_events')
    return render_template('upcoming_events.html')

@app.route('/events/past')
def past_events():
    analytics.track_page_view('past_events')
    return render_template('past_events.html')

@app.route('/events/workshops')
def workshops():
    analytics.track_page_view('workshops')
    return render_template('workshops.html')

@app.route('/community')
def community():
    analytics.track_page_view('community')
    return render_template('community.html')

@app.route('/community/success-stories')
def success_stories():
    analytics.track_page_view('success_stories')
    return render_template('success_stories.html')

@app.route('/community/mentorship')
def mentorship():
    analytics.track_page_view('mentorship')
    return render_template('mentorship.html')

@app.route('/community/forum')
def forum():
    analytics.track_page_view('forum')
    return render_template('forum.html')

@app.route('/resources')
def resources():
    analytics.track_page_view('resources')
    return render_template('resources.html')

@app.route('/resources/resume-builder')
def resume_builder():
    # Redirect to ASU Career Services
    return redirect('https://career.asu.edu/', code=302)

@app.route('/resources/interview-prep')
def interview_prep():
    # Redirect to ASU Career Services
    return redirect('https://career.asu.edu/', code=302)

@app.route('/resources/career-assessment')
def career_assessment():
    # Redirect to ASU Career Services
    return redirect('https://career.asu.edu/', code=302)

@app.route('/resources/networking-guide')
def networking_guide():
    # Redirect to ASU Career Services
    return redirect('https://career.asu.edu/', code=302)

@app.route('/join')
def join():
    analytics.track_page_view('join')
    return render_template('join.html')

@app.route('/api/track-resource-click', methods=['POST'])
def track_resource_click():
    """API endpoint to track resource clicks"""
    data = request.get_json()
    if data and 'resource_name' in data:
        analytics.track_resource_click(data['resource_name'])
        return jsonify({"success": True})
    return jsonify({"success": False, "error": "Missing resource name"})

@app.route('/api/website-stats')
def get_website_stats():
    """API endpoint to get website statistics"""
    return jsonify(analytics.get_analytics_summary())

@app.route('/about')
def about():
    return render_template('about.html')

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 