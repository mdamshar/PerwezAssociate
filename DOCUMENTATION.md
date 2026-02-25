# 🎯 Perwez Associate - Complete Django Website Documentation

## 📋 Project Overview

A complete, production-ready Django full-stack website for **Perwez Associate** - a construction, interior design, and project management company.

**Status**: ✅ Complete and Ready to Use  
**Django Version**: 5.2.11  
**Database**: SQLite3  
**Frontend Framework**: Bootstrap 5  

---

## ✨ Features Implemented

### 🌐 Frontend Features
- ✅ Responsive Navigation Bar with Logo
- ✅ Hero Section with Background & CTA
- ✅ Video Gallery Section
- ✅ 8 Services Display Cards
- ✅ Free Quote Request Form (with 10 topic options)
- ✅ Feedback Form Section
- ✅ Blog Post Display
- ✅ Complete Footer with Contact & Social Media

### 🛠️ Admin Panel Features
- ✅ Blog Post Management (Create, Edit, Delete)
- ✅ Project Portfolio Upload & Management
- ✅ Quote Request Management with Status Tracking
- ✅ Feedback Viewer
- ✅ Excel Export for Quotes (with formatting)
- ✅ Accept/Delete Quote Actions
- ✅ Custom Admin Interface with Filtering

### 💾 Database Models
- ✅ BlogPost (with auto timestamps)
- ✅ QuoteRequest (with status tracking)
- ✅ Feedback (with optional phone field)
- ✅ Category & Portfolio (for services)

---

## 📁 Project Structure

```
Perwez Associate/
│
├── 📄 Core Files
│   ├── manage.py                 # Django management script
│   ├── db.sqlite3                # Database (auto-created)
│   ├── .gitignore                # Git ignore rules
│   ├── requirements.txt           # Python dependencies
│   ├── setup_project.py           # Initial setup script
│   ├── run_server.bat             # Windows batch starter
│   ├── run_server.ps1             # PowerShell starter
│   ├── README.md                  # Full documentation
│   └── QUICK_START.md             # Quick start guide
│
├── 📦 Django Configuration (perwez_config/)
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL routing
│   ├── wsgi.py                   # WSGI app
│   ├── asgi.py                   # ASGI app
│   └── __init__.py
│
├── 🏠 Home App (home/)
│   ├── models.py                 # Category, Portfolio models
│   ├── views.py                  # Home page view
│   ├── admin.py                  # Admin customization
│   ├── apps.py
│   ├── tests.py
│   ├── migrations/
│   └── __init__.py
│
├── 📝 Blog App (blog/)
│   ├── models.py                 # BlogPost model
│   ├── views.py                  # Blog list & detail views
│   ├── urls.py                   # Blog URL patterns
│   ├── admin.py                  # Blog admin
│   ├── apps.py
│   ├── migrations/
│   └── __init__.py
│
├── 📋 Forms App (forms_app/)
│   ├── models.py                 # QuoteRequest, Feedback models
│   ├── forms.py                  # Django forms
│   ├── views.py                  # Form handling views
│   ├── urls.py                   # Forms URL patterns
│   ├── admin.py                  # Admin with Excel export
│   ├── apps.py
│   ├── migrations/
│   └── __init__.py
│
├── 🎨 Templates (templates/)
│   ├── base.html                 # Base template (nav + footer)
│   ├── index.html                # Home page
│   ├── blog/
│   │   ├── blog_list.html        # Blog listing
│   │   └── blog_detail.html      # Blog detail page
│   └── forms/
│       ├── quote_form.html       # Quote request form
│       └── feedback_form.html    # Feedback form
│
├── 🎨 Static Files (static/)
│   ├── css/
│   │   └── style.css             # Custom styles
│   ├── js/
│   │   └── script.js             # JavaScript functionality
│   └── images/
│       ├── logo.png              # Company logo
│       └── section2.mp4          # Project video
│
├── 💾 Media Files (media/)
│   ├── blog/                     # Blog post images
│   └── portfolio/                # Portfolio project images
│
└── 🗂️ Other Files
    └── staticfiles/              # Collected static files (production)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Quick Setup (5 minutes)

**Option 1: Run Batch Script (Windows)**
```batch
run_server.bat
```

**Option 2: Run PowerShell Script (Windows)**
```powershell
powershell -ExecutionPolicy Bypass -File run_server.ps1
```

**Option 3: Manual Setup**
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations
python manage.py migrate

# 3. Initialize project with superuser & data
python setup_project.py

# 4. Start development server
python manage.py runserver
```

### Access the Application
- **Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **Credentials**: 
  - Username: `admin`
  - Password: `admin123`

---

## 📱 Website Sections Detailed

### 1️⃣ Navigation Bar
```
[Logo] Perwez Associate | Home | About | Services | Blog | [Call Now Button]
```
- Sticky navigation that stays on top while scrolling
- Mobile responsive hamburger menu
- Logo links to home page
- "Call Now" button directs to quote form

### 2️⃣ Hero Section
```
Background Image + Gradient Overlay
┌─────────────────────────────────────┐
│  Transform Your Space Into Reality  │
│  Professional Design & Construction │
│                                     │
│  [Our Services] ← CTA Button        │
└─────────────────────────────────────┘
```
- Full-width hero with background image
- Bold heading with brand message
- Call-to-action button for services

### 3️⃣ About Section
```
┌────────────┬────────────┐
│ Description│  Image     │
│ of Company │  Banner    │
└────────────┴────────────┘
```
- Company introduction
- Professional background image
- Two-column responsive layout

### 4️⃣ Video Gallery Section
```
┌──────────────────────────┐
│   [Video Player]         │
│   (section2.mp4)         │
└──────────────────────────┘
   [Watch More Gallery]
```
- Embedded video player
- Video file: `section2.mp4`
- Link to full blog/project gallery

### 5️⃣ Services Section (8 Cards)
```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Residential  │  │ Commercial   │  │ Hospitality  │  │ Space        │
│ Design       │  │ Design       │  │ Design       │  │ Planning     │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘

┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Working      │  │ 3D           │  │ Renovation & │  │ Interior     │
│ Drawing      │  │ Visualization│  │ Remodeling   │  │ Styling      │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
```
- 8 service cards in responsive grid
- Hover animations
- Icon display
- Short service descriptions

### 6️⃣ Get Free Quote Section
```
Blue Background Section
┌────────────────────────────┐
│ Get Free Quote             │
├────────────────────────────┤
│ ☐ Your Name                │
│ ☐ Phone Number             │
│ ☐ Address                  │
│ ☐ Topic [Dropdown ▼]       │
│ ☐ Your Message             │
├────────────────────────────┤
│  [Send Request Button]     │
└────────────────────────────┘
```
- Embedded quote form (no separate page)
- 10 Topic options (dropdown)
- Form validation
- Auto-saves to database

**Topic Options:**
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

### 7️⃣ Feedback Section
```
┌────────────────────────────┐
│ We'd Love Your Feedback    │
│ Help us improve our service│
│                            │
│  [Contact Now Button]      │
└────────────────────────────┘
```
- Call to action for feedback
- Opens dedicated feedback form
- Optional mobile number field

### 8️⃣ Footer Section
```
┌──────────────┬──────────────┬──────────────┐
│ Company Info │ Contact Info │ Social Links │
├──────────────┼──────────────┼──────────────┤
│ [Logo]       │ Phone:       │ Instagram    │
│ Perwez Assoc │ +91 747...   │ WhatsApp     │
│ Interior &   │ +91 969...   │ LinkedIn     │
│ Construction │ Email:       │ Facebook     │
│              │ perwez...    │              │
└──────────────┴──────────────┴──────────────┘
Copyright © 2026 Perwez Associate
```

**Contact Information:**
- Phone 1: +91 7479889661
- Phone 2: +91 9693751969
- Email: perwezassociate.work@gmail.com

**Social Media:**
- Instagram: https://www.instagram.com/perwez_associate/
- WhatsApp: https://whatsapp.com/channel/0029VbCXFOG8F2pEs6GHjQ1V
- LinkedIn: https://www.linkedin.com/company/perwez_associate
- Facebook: https://www.facebook.com/perwez_associate

---

## 🛠️ Admin Panel Complete Guide

### Admin Access
1. Go to: http://localhost:8000/admin
2. Login: `admin` / `admin123`

### Section 1: Blog Management

**Create Blog Post**
```
Admin > Blog Posts > Add Blog Post
├─ Title (required)
│  └─ Text input field
├─ Description (required)
│  └─ Text area for content
├─ Image (optional)
│  └─ Image upload field
└─ Timestamps (auto-generated)
   ├─ created_at: Auto-set on creation
   └─ updated_at: Auto-updated on edit
```

**Actions Available:**
- ✏️ Edit existing posts
- 🗑️ Delete posts
- 🔍 Search by title/description
- 📅 Filter by date

### Section 2: Project Portfolio

**Upload Project**
```
Admin > Portfolios > Add Portfolio
├─ Title (required)
├─ Description (required)
├─ Category (required)
│  └─ Dropdown: Choose service category
├─ Image (required)
│  └─ Project image upload
└─ Created At (auto)
```

**Available Categories:**
- Residential Design
- Commercial Design
- Hospitality Design
- Space Planning
- Working Drawing
- 3D Visualization
- Renovation & Remodeling
- Interior Styling

### Section 3: Quote Request Management

**View Quotes**
```
Admin > Quote Requests > All Quotes
├─ List View showing:
│  ├─ Customer Name
│  ├─ Phone Number
│  ├─ Service Topic
│  ├─ Status (Pending/Accepted/Deleted)
│  └─ Created Date
├─ Filter Options:
│  ├─ By Status
│  ├─ By Topic
│  └─ By Date Range
└─ Search: By name or phone
```

**Quote Details**
```
Quote Information Box
├─ Contact Information
│  ├─ Name
│  ├─ Phone
│  └─ Address
├─ Request Details
│  ├─ Topic
│  └─ Message
└─ Status: [Pending ▼]
```

**Actions on Quotes**

1. **Accept Quote**
   - Checkbox > "Mark as Accepted" > Go
   - Status changes to "Accepted"
   - Stored separately for reference

2. **Delete Quote**
   - Checkbox > "Mark as Deleted" > Go
   - Status changes to "Deleted"
   - Removed from pending view
   - Can be viewed in "Deleted" status filter

3. **Download as Excel**
   - Select quotes > "Download selected quotes as Excel" > Go
   - Creates beautifully formatted Excel file with:
     - All quote information
     - Headers in blue with white text
     - Formatted columns
     - Timestamp information
   - File name: `quotes_YYYYMMDD_HHMMSS.xlsx`

### Section 4: Feedback Viewer

**View Feedback**
```
Admin > Feedback > All Feedback
├─ List Display:
│  ├─ Customer Name
│  ├─ Mobile (if provided)
│  └─ Date Received
├─ Filter by:
│  └─ Creation Date
└─ Search: By name, phone, or message
```

**Feedback Details**
```
Feedback Item
├─ Name (required)
├─ Mobile (optional)
├─ Message (full text)
└─ Created Date & Time
```

**Management:**
- 👁️ View full feedback message
- 🗑️ Delete unwanted feedback
- 📋 No add permission (form submission only)

---

## 📊 Database Schema

### QuoteRequest Model
```python
Fields:
├─ id: Integer (Primary Key)
├─ name: String(100) - Customer name
├─ phone: String(20) - Contact number
├─ address: Text - Full address
├─ topic: String(50) - Service choice
├─ message: Text - Detailed message
├─ status: String(20) - Pending/Accepted/Deleted
├─ created_at: DateTime - Submission time
└─ updated_at: DateTime - Last modification
```

### Feedback Model
```python
Fields:
├─ id: Integer (Primary Key)
├─ name: String(100) - Customer name
├─ mobile: String(20) - Optional phone
├─ message: Text - Feedback message
└─ created_at: DateTime - Submission time
```

### BlogPost Model
```python
Fields:
├─ id: Integer (Primary Key)
├─ title: String(200) - Post title
├─ description: Text - Post content
├─ image: ImageField - Optional image
├─ created_at: DateTime - Auto timestamp
└─ updated_at: DateTime - Auto timestamp
```

### Category Model
```python
Fields:
├─ id: Integer (Primary Key)
├─ name: String(100) - Unique category name
└─ description: Text - Optional description
```

### Portfolio Model
```python
Fields:
├─ id: Integer (Primary Key)
├─ title: String(200) - Project name
├─ description: Text - Project details
├─ category: ForeignKey - Service type
├─ image: ImageField - Project image
└─ created_at: DateTime - Creation date
```

---

## 🎯 Form Handling

### Quote Request Form Workflow
```
User fills form
    ↓
Client-side validation (HTML5)
    ↓
Submit to /forms/quote/
    ↓
Django validates (server-side)
    ↓
Save to QuoteRequest model
    ↓
Success message displayed
    ↓
Redirect to home
    ↓
Admin receives notification (model saved)
```

### Feedback Form Workflow
```
User fills form
    ↓
Client-side validation
    ↓
Submit to /forms/feedback/
    ↓
Django validates
    ↓
Save to Feedback model
    ↓
Success message
    ↓
Redirect to home
```

---

## 🎨 Customization Guide

### Change Company Logo
```
1. Replace file: static/images/logo.png
2. Use same filename or update:
   - templates/base.html (navbar logo)
   - templates/base.html (footer logo)
```

### Change Contact Information
**File**: `templates/base.html`
```html
<!-- In footer section, replace: -->
<a href="tel:+917479889661">+91 7479889661</a>
<a href="tel:+919693751969">+91 9693751969</a>
<a href="mailto:perwezassociate.work@gmail.com">Email</a>
```

### Change Social Media Links
**File**: `templates/base.html`
```html
<!-- Update in footer: -->
<a href="https://www.instagram.com/perwez_associate/">Instagram</a>
<a href="https://whatsapp.com/channel/0029VbCXFOG8F2pEs6GHjQ1V">WhatsApp</a>
<a href="https://www.linkedin.com/company/perwez_associate">LinkedIn</a>
<a href="https://www.facebook.com/perwez_associate">Facebook</a>
```

### Change Hero Background
**File**: `templates/index.html`
```html
<!-- Replace image URL in hero section: -->
style="background: linear-gradient(...), url('YOUR_NEW_IMAGE_URL')"
```

### Customize Colors
**File**: `static/css/style.css`
```css
/* Primary colors */
--primary-color: #007bff;    /* Blue */
--warning-color: #ffc107;    /* Yellow */
--dark-color: #333;          /* Dark Gray */

/* All CSS variables at top of file */
```

---

## 🔐 Security & Production Tips

### Before Going Live
1. **Change SECRET_KEY**
   ```python
   # In perwez_config/settings.py
   SECRET_KEY = 'your-new-secret-key-here'
   ```

2. **Set DEBUG = False**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

3. **Use PostgreSQL instead of SQLite**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'perwez_db',
           'USER': 'postgres',
           'PASSWORD': 'secure_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. **Configure Email Backend**
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@gmail.com'
   EMAIL_HOST_PASSWORD = 'your-app-password'
   ```

5. **Install HTTPS Certificate**
   - Use Let's Encrypt (free)
   - Set SECURE_SSL_REDIRECT = True

6. **Enable CORS if needed**
   ```bash
   pip install django-cors-headers
   ```

---

## 📈 Performance Optimization

### Enable Caching
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
```

### Compress Static Files
```bash
# For production
python manage.py compress
```

### Use CDN for Static Files
```python
# Configure S3 or CloudFront
STATIC_URL = 'https://cdn.yourdomain.com/static/'
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8000 in use | `python manage.py runserver 8001` |
| Images not showing | Check `/media/` folder permissions |
| CSS not loading | Clear cache (Ctrl+Shift+Delete) |
| Database locked | Delete `db.sqlite3` and remigrate |
| Forms not working | Check CSRF tokens in templates |
| Email not sending | Configure EMAIL_BACKEND in settings |

---

## 📚 File Locations Reference

| Item | Location |
|------|----------|
| Logo | `static/images/logo.png` |
| Video | `static/images/section2.mp4` |
| CSS | `static/css/style.css` |
| JavaScript | `static/js/script.js` |
| Blog Images | `media/blog/` |
| Portfolio Images | `media/portfolio/` |
| Base Template | `templates/base.html` |
| Home Template | `templates/index.html` |
| Database | `db.sqlite3` |
| Config | `perwez_config/settings.py` |

---

## 📞 Support

For technical issues or feature requests:
- **Email**: perwezassociate.work@gmail.com
- **Phone**: +91 7479889661
- **Website**: (In Development)

---

## 📄 License

This project is proprietary to Perwez Associate. All rights reserved. © 2026

---

## 🎉 Congratulations!

Your Perwez Associate website is now complete and ready to use!

**Key Files to Remember:**
- ✅ `run_server.bat` - Start server (Windows)
- ✅ `run_server.ps1` - Start server (PowerShell)
- ✅ `setup_project.py` - Initialize database
- ✅ `README.md` - Full documentation
- ✅ `QUICK_START.md` - Quick reference

**Next Steps:**
1. Add your company information
2. Upload projects and portfolio items
3. Create blog posts
4. Customize styling
5. Deploy to production

---

**Version**: 1.0.0  
**Created**: February 2026  
**Status**: Production Ready ✅
