# Global Career Network (GCN) Website

A Flask-based website for the Global Career Network student organization at Arizona State University. This website serves as a platform for international students to access career development resources, networking opportunities, and professional guidance.

## Features

- **Responsive Design**: Modern, mobile-friendly interface with ASU branding
- **Static Pages**: Home, Team, Events, Community, and Join pages
- **Resource Redirects**: All resource pages redirect to ASU Career Services
- **Interactive Elements**: Smooth animations, hover effects, and form validation
- **Accessibility**: WCAG compliant with proper semantic HTML and ARIA labels
- **Security**: Content Security Policy and other security headers implemented

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with ASU color scheme
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)

## Project Structure

```
GCN_WEBSITE/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   └── main.js       # JavaScript functionality
│   └── images/           # Images and media files
└── templates/            # HTML templates
    ├── base.html         # Base template
    ├── index.html        # Home page
    ├── team.html         # Team page
    ├── events.html       # Events overview
    ├── upcoming_events.html
    ├── past_events.html
    ├── workshops.html
    ├── community.html    # Community overview
    ├── success_stories.html
    ├── mentorship.html
    ├── forum.html
    ├── join.html         # Membership form
    ├── 404.html          # Error pages
    └── 500.html
```

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd GCN_WEBSITE
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the website**:
   Open your browser and navigate to `http://localhost:5000`

## Deployment

### For GitHub Pages (Static Hosting)

Since this is a Flask application, you'll need to convert it to static files for GitHub Pages hosting:

1. **Install Flask-Freeze**:
   ```bash
   pip install Flask-Freeze
   ```

2. **Add to app.py**:
   ```python
   from flask_frozen import Freezer
   freezer = Freezer(app)
   
   if __name__ == '__main__':
       freezer.freeze()
   ```

3. **Generate static files**:
   ```bash
   python app.py
   ```

4. **Deploy the `build` folder** to GitHub Pages

### For Traditional Hosting

1. **Set up a web server** (Apache, Nginx, etc.)
2. **Configure WSGI** with your hosting provider
3. **Upload the application files**
4. **Install dependencies** on the server
5. **Configure environment variables** if needed

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

1. **Create a new template** in the `templates/` directory
2. **Add a route** in `app.py`:
   ```python
   @app.route('/new-page')
   def new_page():
       return render_template('new_page.html')
   ```

### Modifying Styles

- Main styles are in `static/css/style.css`
- Page-specific styles can be added in individual templates
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