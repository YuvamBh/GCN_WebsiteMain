# Global Career Network (GCN) Website

A static website for the Global Career Network student organization at Arizona State University. This website serves as a platform for international students to access career development resources, networking opportunities, and professional guidance.

## Features

- **Responsive Design**: Modern, mobile-friendly interface with ASU branding
- **Static Pages**: Home, Team, Events, Community, and Join pages
- **Resource Redirects**: All resource pages redirect to ASU Career Services
- **Interactive Elements**: Smooth animations, hover effects, and form validation
- **Accessibility**: WCAG compliant with proper semantic HTML and ARIA labels
- **Security**: Content Security Policy and other security headers implemented
- **Static Form Handling**: Feedback forms work without backend using Netlify Forms

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with ASU color scheme
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)
- **Form Handling**: Netlify Forms (for static deployment)
- **Deployment**: Netlify or Vercel (static hosting)

## Project Structure

```
GCN_WEBSITE/
├── index.html            # Home page (static)
├── team.html             # Team page (static)
├── events.html           # Events page (static)
├── community.html        # Community page (static)
├── join.html             # Join page (static)
├── resources.html        # Resources page (static)
├── 404.html              # Error page (static)
├── 500.html              # Error page (static)
├── netlify.toml          # Netlify deployment config
├── vercel.json           # Vercel deployment config
├── README.md             # Project documentation
├── CODEBASE_ANALYSIS.md  # Refactoring analysis
├── static/               # Static assets
│   ├── css/
│   │   ├── style.css     # Main stylesheet
│   │   ├── index.css     # Home page styles
│   │   └── feedback.css  # Feedback form styles
│   ├── js/
│   │   ├── main.js       # Main JavaScript
│   │   ├── navigation.js # Navigation functionality
│   │   ├── feedback.js   # Feedback form handling
│   │   └── index.js      # Home page JavaScript
│   └── images/           # Images and media files
└── templates/            # Original Flask templates (disabled)
    ├── base.html         # Base template (converted to static)
    ├── index.html        # Home template (converted to static)
    └── ...               # Other templates (converted to static)
```

## Quick Start (Static Site)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd GCN_WEBSITE
   ```

2. **Serve the static files locally**:
   ```bash
   # Option 1: Using Python's built-in server
   python -m http.server 8000
   
   # Option 2: Using Node.js serve
   npx serve .
   
   # Option 3: Using any static file server
   ```

3. **Access the website**:
   Open your browser and navigate to `http://localhost:8000`

## Local Development

The website is now a static site that can be served by any web server. No Python backend is required.

### Using Python's HTTP Server
```bash
python -m http.server 8000
```

### Using Node.js serve
```bash
npx serve .
```

### Using any other static file server
Any web server that can serve static files will work (Apache, Nginx, etc.)

## Deployment

The website is now a static site that can be deployed to any static hosting service.

### Netlify Deployment (Recommended)

1. **Connect your repository to Netlify**:
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub/GitLab repository
   - Select the repository containing this code

2. **Configure build settings**:
   - Build command: (leave empty - no build needed)
   - Publish directory: `.` (root directory)
   - The `netlify.toml` file will handle all configuration

3. **Deploy**:
   - Netlify will automatically deploy your site
   - Your site will be available at `https://your-site-name.netlify.app`

4. **Form handling**:
   - Netlify Forms will automatically handle the feedback form
   - Form submissions will appear in your Netlify dashboard
   - No additional configuration needed

### Vercel Deployment

1. **Connect your repository to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Connect your GitHub/GitLab repository
   - Select the repository containing this code

2. **Configure deployment**:
   - Framework Preset: "Other"
   - Build Command: (leave empty)
   - Output Directory: `.` (root directory)
   - The `vercel.json` file will handle all configuration

3. **Deploy**:
   - Vercel will automatically deploy your site
   - Your site will be available at `https://your-site-name.vercel.app`

### GitHub Pages Deployment

1. **Enable GitHub Pages**:
   - Go to your repository settings
   - Scroll to "Pages" section
   - Select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder

2. **Deploy**:
   - GitHub Pages will automatically deploy your site
   - Your site will be available at `https://your-username.github.io/your-repo-name`

### Other Static Hosting Services

The website can be deployed to any static hosting service:
- **AWS S3 + CloudFront**
- **Google Cloud Storage**
- **Azure Static Web Apps**
- **Firebase Hosting**
- **Surge.sh**
- **Any web server** (Apache, Nginx, etc.)

## Refactoring Summary

This website has been refactored from a Flask-based backend application to a static frontend-only site. Here are the key changes:

### What Was Changed

1. **Backend Disabled**: All Python Flask code has been commented out with explanatory comments
2. **Templates Converted**: Flask templates converted to static HTML files
3. **Form Handling**: Python backend form processing replaced with Netlify Forms
4. **Static Assets**: All CSS, JavaScript, and images remain unchanged
5. **Deployment Ready**: Added configuration files for Netlify and Vercel

### Files Modified

- **`app.py`**: Commented out with explanation of why disabled
- **`enhanced_features.py`**: Commented out with explanation of why disabled  
- **`requirements.txt`**: Commented out with explanation of why disabled
- **`static/js/feedback.js`**: Updated to use Netlify Forms instead of Python backend
- **Templates**: Converted from Jinja2 to static HTML

### Form Handling

The feedback form now uses **Netlify Forms** for static deployment:

- **Netlify Forms**: Automatically handles form submissions when deployed to Netlify
- **Formspree**: Alternative option for other hosting providers
- **No Backend Required**: Forms work without any server-side processing

### Re-enabling Backend (If Needed)

If you need to re-enable the Python backend:

1. **Uncomment the backend files**:
   - Remove comment blocks from `app.py`
   - Remove comment blocks from `enhanced_features.py`
   - Restore `requirements.txt` dependencies

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:
   ```bash
   python app.py
   ```

4. **Access at**: `http://localhost:5000`

## Customization

### Colors and Branding

The website uses ASU's official colors defined in CSS variables:

```css
:root {
  --asu-maroon: #8C1D40;
  --asu-gold: #FFC627;
  --asu-black: #121212;
  --asu-white: #FFFFFF;
}
```

### Adding New Pages

1. **Create a new HTML file** in the root directory (e.g., `new-page.html`)
2. **Copy the structure** from existing pages
3. **Update navigation** in all HTML files to include the new page
4. **Add any page-specific CSS** to `static/css/`

### Modifying Styles

- Main styles are in `static/css/style.css`
- Page-specific styles can be added in individual HTML files
- Responsive design breakpoints are defined for mobile optimization

## Features Overview

### Home Page
- Hero section with call-to-action buttons
- Features highlighting GCN benefits
- Statistics section
- About GCN section
- Testimonials and employer relations

### Team Page
- Team member cards with photos and descriptions
- Social media links
- Mission statement

### Events Section
- Upcoming events with registration
- Past events with materials access
- Workshop categories and descriptions

### Community Section
- Success stories from members
- Mentorship program information
- Discussion forum guidelines

### Join Page
- Membership benefits overview
- Registration form with validation
- Career interests and goals collection

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- Optimized images and assets
- Minified CSS and JavaScript (for production)
- Lazy loading for images
- Efficient CSS animations
- Responsive image loading

## Security Features

- Content Security Policy headers
- XSS protection
- CSRF protection (if forms are implemented)
- Secure headers configuration
- Input validation and sanitization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and organizational use. Please respect ASU's branding guidelines when modifying the design.

## Contact

For questions or support, contact the GCN team at gcn@asu.edu

## Acknowledgments

- Arizona State University for branding and support
- Original Next.js website team for design inspiration
- Flask community for the excellent framework
- Font Awesome for icons
- Google Fonts for typography 