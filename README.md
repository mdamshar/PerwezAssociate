# Perwez Associate - Django Full Stack Website

A professional Django full-stack website for Perwez Associate, specializing in construction, interior design, and project management.

## Features

### Frontend Features
- **Responsive Design** - Mobile-friendly layout with Bootstrap 5
- **Hero Section** - Eye-catching banner with call-to-action
- **Video Gallery** - Embedded video showcase of projects
- **Services Display** - 8 service categories showcased
- **Free Quote Form** - Customers can request quotes
- **Feedback Section** - Users can submit feedback
- **Blog Section** - Read and browse blog posts
- **Footer** - Contact information and social media links

### Admin Panel Features
- **Blog Management** - Create, edit, and delete blog posts
- **Project Portfolio** - Upload and manage projects
- **Quote Management** - View received quote requests with:
  - Accept/Delete options
  - Download as Excel
  - Status filtering (Pending, Accepted, Deleted)
- **Feedback Management** - View and manage customer feedback
- **Excel Export** - Download quotes and details as Excel files

## Project Structure

```
Perwez Associate/
├── perwez_config/          # Main Django configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI application
├── home/                   # Home app
│   ├── models.py           # Category, Portfolio models
│   ├── views.py            # Home views
│   └── admin.py            # Admin customization
├── blog/                   # Blog app
│   ├── models.py           # BlogPost model
│   ├── views.py            # Blog views
│   ├── urls.py             # Blog URLs
│   └── admin.py            # Blog admin
├── forms_app/              # Forms app
│   ├── models.py           # QuoteRequest, Feedback models
│   ├── forms.py            # Django forms
│   ├── views.py            # Form views
│   ├── urls.py             # Forms URLs
│   └── admin.py            # Forms admin with Excel export
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── index.html          # Home page
│   ├── blog/               # Blog templates
│   └── forms/              # Form templates
├── static/                 # Static files
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Images and videos
├── media/                  # User uploaded files
├── manage.py               # Django management script
└── setup_project.py        # Initial setup script
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Run Setup Script

```bash
python setup_project.py
```

This will:
- Create admin superuser (username: `admin`, password: `admin123`)
- Create service categories
- Create sample blog post

### Step 4: Start Development Server

```bash
python manage.py runserver
```

The website will be available at: **http://localhost:8000**

### Admin Panel

Access admin panel at: **http://localhost:8000/admin**

**Login Credentials:**
- Username: `admin`
- Password: `admin123`

## Usage

### For Website Visitors

1. **Homepage** - View hero section, services, and portfolio
2. **Blog** - Browse and read blog posts
3. **Get Free Quote** - Fill form to request a quote
4. **Send Feedback** - Share feedback about our services
5. **Contact** - Use footer contact information

### For Admin Users

#### Creating Blog Posts
1. Go to Admin > Blog Posts
2. Click "Add Blog Post"
3. Fill in:
   - Title
   - Description
   - Image (optional)
4. Save (Created date is automatic)

#### Uploading Projects
1. Go to Admin > Portfolios
2. Click "Add Portfolio"
3. Fill in:
   - Title
   - Description
   - Category (choose from services)
   - Image

#### Managing Quote Requests
1. Go to Admin > Quote Requests
2. View all pending quotes
3. Options:
   - **Accept** - Mark as accepted and move to accepted section
   - **Delete** - Mark as deleted and move to deleted section
   - **Download** - Export selected quotes as Excel
4. Filter by status: Pending, Accepted, Deleted

#### Managing Feedback
1. Go to Admin > Feedback
2. View all received feedback
3. Delete unwanted feedback
4. View customer contact information

## Models

### QuoteRequest
- Name, Phone, Address
- Topic (dropdown with 10 options)
- Message
- Status (Pending, Accepted, Deleted)
- Timestamps

### Feedback
- Name (required)
- Mobile (optional)
- Message
- Created timestamp

### BlogPost
- Title
- Description
- Image
- Auto timestamps

### Category & Portfolio
- Category names for services
- Portfolio items with images and descriptions

## Contact Information

- **Phone**: +91 7479889661, +91 9693751969
- **Email**: perwezassociate.work@gmail.com
- **Instagram**: https://www.instagram.com/perwez_associate/
- **WhatsApp**: https://whatsapp.com/channel/0029VbCXFOG8F2pEs6GHjQ1V
- **LinkedIn**: https://www.linkedin.com/company/perwez_associate
- **Facebook**: https://www.facebook.com/perwez_associate

## Services Offered

1. Residential Design
2. Commercial Design
3. Hospitality Design
4. Space Planning
5. Working Drawing
6. 3D Visualization
7. Renovation & Remodeling
8. Interior Styling
9. Project Planning
10. General Contracting

## Technologies Used

- **Backend**: Django 5.2.11
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite3 (development)
- **Image Processing**: Pillow
- **Excel Export**: openpyxl
- **Forms**: django-crispy-forms

## Customization

### Change Colors
Edit `static/css/style.css` to customize colors and styling.

### Change Contact Information
Edit `templates/base.html` footer section to update:
- Phone numbers
- Email
- Social media links

### Change Logo
Replace `static/images/logo.png` with your logo image.

### Change Hero Background
Edit `templates/index.html` hero section image URL.

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in `settings.py`
2. Update `ALLOWED_HOSTS` in `settings.py`
3. Change `SECRET_KEY` to a secure value
4. Configure a production database (PostgreSQL recommended)
5. Set up email backend for form notifications
6. Use a production WSGI server (Gunicorn)
7. Set up static file serving (CDN or whitenoise)

## Development Tips

### Create New Blog Post
```python
python manage.py shell
from blog.models import BlogPost
BlogPost.objects.create(
    title="Your Title",
    description="Your Description",
    # image=... (optional)
)
```

### Export Quotes to Excel
1. Login to admin
2. Go to Quote Requests
3. Select quotes
4. Choose "Download selected quotes as Excel" action

### Custom Admin Actions
All models have custom admin actions for management and exports.

## Troubleshooting

### Port 8000 Already in Use
```bash
python manage.py runserver 8001
```

### Database Errors
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Changes Not Showing
- Clear browser cache (Ctrl+Shift+Delete)
- Restart development server

## Support & Maintenance

For issues or feature requests, contact Perwez Associate at:
- Email: perwezassociate.work@gmail.com
- Phone: +91 7479889661

## License

This project is proprietary to Perwez Associate. All rights reserved.

---

**Version**: 1.0.0
**Last Updated**: February 2026
