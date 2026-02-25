# Perwez Associate - Quick Start Guide

## 🚀 Quick Setup (2 minutes)

### 1. Install & Setup
```bash
cd "d:\All Courses\PYTHON CODE\PROJECTSFILE\Parwez Associate"
pip install -r requirements.txt
python manage.py migrate
python setup_project.py
```

### 2. Start Server
```bash
python manage.py runserver
```

### 3. Access Website
- **Frontend**: http://localhost:8000
- **Admin**: http://localhost:8000/admin
- **Credentials**: username `admin` / password `admin123`

---

## 📱 Website Sections

### ✅ Navigation Bar
- Logo (static/images/logo.png)
- Home, About, Services, Blog links
- "Call Now" button (goes to quote form)

### ✅ Hero Section
- Background image with gradient overlay
- Large heading: "Transform Your Space Into Reality"
- Call-to-action button: "Our Services"

### ✅ About Section
- Description of Perwez Associate
- Image showcase

### ✅ Video Section
- Embedded video (static/images/section2.mp4)
- "Watch More Project Gallery" button

### ✅ Services Section (8 Services)
- Residential Design
- Commercial Design
- Hospitality Design
- Space Planning
- Working Drawing
- 3D Visualization
- Renovation & Remodeling
- Interior Styling

### ✅ Get Free Quote Section
- Form with fields:
  - Name
  - Phone
  - Address
  - Topic (dropdown)
  - Message
- Submit button sends data to admin

### ✅ Feedback Section
- "We'd Love Your Feedback" heading
- "Contact Now" button opens feedback form
- Form collects: Name, Mobile (optional), Message

### ✅ Footer
- Logo + Company name
- Contact details:
  - Phones: +91 7479889661, +91 9693751969
  - Email: perwezassociate.work@gmail.com
- Social media links:
  - Instagram: https://www.instagram.com/perwez_associate/
  - WhatsApp: https://whatsapp.com/channel/0029VbCXFOG8F2pEs6GHjQ1V
  - LinkedIn: https://www.linkedin.com/company/perwez_associate
  - Facebook: https://www.facebook.com/perwez_associate

---

## 👨‍💼 Admin Panel Guide

### Access Admin
1. Go to http://localhost:8000/admin
2. Login with: admin / admin123

### 1️⃣ Create Blog Post
```
Admin > Blog Posts > Add Blog Post
- Title: (required)
- Description: (required)
- Image: (optional, PNG/JPG)
- Created at: (auto-generated)
```

### 2️⃣ Upload Project
```
Admin > Portfolios > Add Portfolio
- Title: (required)
- Description: (required)
- Category: (choose one)
- Image: (required)
- Created at: (auto-generated)
```

### 3️⃣ Manage Received Quotes
```
Admin > Quote Requests
- View all customer quote requests
- Actions available:
  * ✅ Mark as Accepted (stores in accepted section)
  * ❌ Mark as Deleted (moves to deleted section)
  * 📊 Download as Excel (export to spreadsheet)
- Filter by status: Pending, Accepted, Deleted
```

### 4️⃣ View Feedback
```
Admin > Feedback
- See all customer feedback
- Customer name, optional phone, message
- Can delete unwanted feedback
```

### 5️⃣ Export Data
```
Quote Requests > Select quotes > "Download as Excel"
- Exports with columns:
  * Name, Phone, Address, Topic
  * Message, Status, Created At, Updated At
```

---

## 💾 Database Models

### QuoteRequest
```python
- name: CharField (max 100)
- phone: CharField (max 20)
- address: TextField
- topic: ChoiceField (10 options)
- message: TextField
- status: Pending/Accepted/Deleted
- created_at: DateTime (auto)
- updated_at: DateTime (auto)
```

### Feedback
```python
- name: CharField (max 100)
- mobile: CharField (optional, max 20)
- message: TextField
- created_at: DateTime (auto)
```

### BlogPost
```python
- title: CharField (max 200)
- description: TextField
- image: ImageField (optional)
- created_at: DateTime (auto)
- updated_at: DateTime (auto)
```

### Category
```python
- name: CharField (unique, max 100)
- description: TextField (optional)
```

### Portfolio
```python
- title: CharField (max 200)
- description: TextField
- category: ForeignKey (links to Category)
- image: ImageField
- created_at: DateTime (auto)
```

---

## 🎨 Customization

### Change Logo
Replace: `static/images/logo.png`

### Change Colors
Edit: `static/css/style.css`
- Primary color: `#007bff` (blue)
- Warning color: `#ffc107` (yellow)
- Dark color: `#333`

### Change Contact Info
Edit: `templates/base.html` (footer section)
- Phone numbers
- Email address
- Social media URLs

### Change Hero Image
Edit: `templates/index.html`
- Replace the URL in hero section background

---

## 📁 File Uploads

### Blog Post Images
Location: `/media/blog/`
Supported: PNG, JPG, JPEG, GIF

### Portfolio Images
Location: `/media/portfolio/`
Supported: PNG, JPG, JPEG, GIF

### Static Assets
- Logo: `static/images/logo.png`
- Video: `static/images/section2.mp4`
- CSS: `static/css/style.css`
- JS: `static/js/script.js`

---

## 🔗 URL Routes

| URL | Purpose |
|-----|---------|
| `/` | Home page |
| `/admin/` | Admin panel |
| `/blog/` | Blog list |
| `/blog/<id>/` | Blog detail |
| `/forms/quote/` | Quote form |
| `/forms/feedback/` | Feedback form |

---

## 🛠️ Common Tasks

### Collect Static Files
```bash
python manage.py collectstatic
```

### Create Backup
```bash
python manage.py dumpdata > backup.json
```

### Restore Backup
```bash
python manage.py loaddata backup.json
```

### Reset Database
```bash
del db.sqlite3
python manage.py migrate
python setup_project.py
```

### View All Quotes
```bash
python manage.py shell
from forms_app.models import QuoteRequest
QuoteRequest.objects.all()
```

---

## ⚠️ Troubleshooting

**Problem**: Port 8000 in use
**Solution**: `python manage.py runserver 8001`

**Problem**: Images not showing
**Solution**: Check `/media/` folder exists and files are uploaded

**Problem**: CSS/JS not loading
**Solution**: Clear browser cache (Ctrl+Shift+Delete)

**Problem**: Database errors
**Solution**: Run `python manage.py migrate --run-syncdb`

---

## 📞 Contact & Support

- **Email**: perwezassociate.work@gmail.com
- **Phone**: +91 7479889661
- **Website**: (In Development)

---

**Version**: 1.0.0 | **Updated**: February 2026
