/* ========================================
   PERWEZ ASSOCIATE - ADMIN PANEL JAVASCRIPT
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {
    initAdminPanel();
});

function initAdminPanel() {
    // Make all sections collapsible
    makeSectionsCollapsible();
    
    // Add toggle button
    addHiddenSectionsToggle();
    
    // Enhance tables
    enhanceTables();
    
    // Add animations
    addAnimations();
    
    // Mobile menu
    setupMobileMenu();
}

// ========= COLLAPSIBLE SECTIONS =========
function makeCollapsible() {
    const sections = document.querySelectorAll('fieldset');
    
    sections.forEach((section, index) => {
        // Wrap in collapsible container
        const wrapper = document.createElement('div');
        wrapper.className = 'admin-section collapsed';
        
        // Create header
        const header = document.createElement('div');
        header.className = 'admin-section-header';
        header.innerHTML = `
            <span>${section.querySelector('legend')?.textContent || 'Section ' + (index + 1)}</span>
            <span class="toggle-icon">▶</span>
        `;
        
        // Create content wrapper
        const content = document.createElement('div');
        content.className = 'admin-section-content';
        
        // Move content
        while (section.children.length > 0) {
            content.appendChild(section.children[0]);
        }
        
        // Assembly
        wrapper.appendChild(header);
        wrapper.appendChild(content);
        section.parentNode.replaceChild(wrapper, section);
        
        // Toggle on click
        header.addEventListener('click', function() {
            wrapper.classList.toggle('collapsed');
            // Save state
            localStorage.setItem('section-' + index, wrapper.classList.contains('collapsed'));
        });
        
        // Restore saved state
        if (localStorage.getItem('section-' + index) === 'false') {
            wrapper.classList.remove('collapsed');
        }
    });
}

function makeFieldsetsHiddenByDefault() {
    const fieldsets = document.querySelectorAll('fieldset');
    
    fieldsets.forEach((fieldset, index) => {
        const legend = fieldset.querySelector('legend');
        if (!legend) return;
        
        // Create wrapper
        const wrapper = document.createElement('div');
        wrapper.className = 'admin-section collapsed';
        
        // Create header
        const header = document.createElement('div');
        header.className = 'admin-section-header';
        header.textContent = legend.textContent;
        
        const icon = document.createElement('span');
        icon.className = 'toggle-icon';
        icon.textContent = '▶';
        header.appendChild(icon);
        
        // Create content wrapper
        const contentWrapper = document.createElement('div');
        contentWrapper.className = 'admin-section-content';
        
        // Move fieldset content
        const allChildren = Array.from(fieldset.children);
        allChildren.forEach(child => {
            contentWrapper.appendChild(child.cloneNode(true));
        });
        
        wrapper.appendChild(header);
        wrapper.appendChild(contentWrapper);
        
        // Toggle functionality
        header.addEventListener('click', function() {
            wrapper.classList.toggle('collapsed');
            icon.style.transform = wrapper.classList.contains('collapsed') ? 'rotate(-90deg)' : 'rotate(0deg)';
            
            // Save state to localStorage
            const sectionName = legend.textContent.trim();
            localStorage.setItem('admin-section-' + sectionName, wrapper.classList.contains('collapsed'));
        });
        
        // Restore saved state
        const sectionName = legend.textContent.trim();
        if (localStorage.getItem('admin-section-' + sectionName) === 'false') {
            wrapper.classList.remove('collapsed');
        }
        
        fieldset.parentNode.replaceChild(wrapper, fieldset);
    });
}

const makeFieldsetsCollapsible = makeFieldsetsHiddenByDefault;

// ========= TABLES ENHANCEMENT =========
function enhanceTables() {
    const tables = document.querySelectorAll('table');
    
    tables.forEach(table => {
        table.classList.add('admin-table');
        
        // Add alternating row colors
        const rows = table.querySelectorAll('tbody tr');
        rows.forEach((row, index) => {
            // Add hover effect
            row.style.transition = 'all 0.3s ease';
        });
        
        // Add sorting capability (optional)
        addTableSorting(table);
    });
}

function addTableSorting(table) {
    const headers = table.querySelectorAll('thead th');
    
    headers.forEach((header, index) => {
        header.style.cursor = 'pointer';
        header.style.userSelect = 'none';
        
        header.addEventListener('click', function() {
            const rows = Array.from(table.querySelectorAll('tbody tr'));
            
            rows.sort((a, b) => {
                const aVal = a.cells[index].textContent.trim();
                const bVal = b.cells[index].textContent.trim();
                
                // Try numeric sort first
                if (!isNaN(aVal) && !isNaN(bVal)) {
                    return parseFloat(aVal) - parseFloat(bVal);
                }
                
                // String sort
                return aVal.localeCompare(bVal);
            });
            
            // Reorder rows
            rows.forEach(row => {
                table.querySelector('tbody').appendChild(row);
            });
        });
    });
}

// ========= HIDDEN SECTIONS TOGGLE =========
function addHiddenSectionsToggle() {
    const button = document.createElement('button');
    button.className = 'hidden-sections-toggle';
    button.innerHTML = '📋 Toggle All Sections';
    button.style.display = 'none'; // Hidden by default
    
    document.body.appendChild(button);
    
    button.addEventListener('click', function() {
        const sections = document.querySelectorAll('.admin-section');
        let allCollapsed = true;
        
        sections.forEach(section => {
            if (!section.classList.contains('collapsed')) {
                allCollapsed = false;
            }
        });
        
        sections.forEach(section => {
            if (allCollapsed) {
                section.classList.remove('collapsed');
            } else {
                section.classList.add('collapsed');
            }
        });
    });
}

// ========= ADD ANIMATIONS =========
function addAnimations() {
    // Animate forms on load
    const forms = document.querySelectorAll('form');
    forms.forEach((form, index) => {
        form.style.animation = `slideIn 0.5s ease ${index * 0.1}s both`;
    });
    
    // Animate fieldsets
    const fieldsets = document.querySelectorAll('fieldset');
    fieldsets.forEach((fieldset, index) => {
        fieldset.style.animation = `fadeIn 0.3s ease ${index * 0.05}s both`;
    });
}

// ========= MOBILE MENU =========
function setupMobileMenu() {
    if (window.innerWidth <= 768) {
        const sidebar = document.querySelector('nav');
        if (!sidebar) return;
        
        sidebar.classList.add('admin-sidebar');
        
        // Create toggle button
        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'mobile-menu-toggle';
        toggleBtn.innerHTML = '☰ Menu';
        toggleBtn.style.cssText = `
            position: fixed;
            top: 20px;
            left: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 8px;
            cursor: pointer;
            z-index: 98;
            font-weight: 600;
        `;
        
        document.body.appendChild(toggleBtn);
        
        toggleBtn.addEventListener('click', function() {
            sidebar.classList.toggle('open');
        });
        
        // Close menu on link click
        const links = sidebar.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', function() {
                sidebar.classList.remove('open');
            });
        });
    }
}

// ========= DARK MODE TOGGLE =========
function addDarkModeToggle() {
    const button = document.createElement('button');
    button.className = 'dark-mode-toggle';
    button.innerHTML = '🌙 Dark Mode';
    button.style.cssText = `
        position: fixed;
        bottom: 100px;
        right: 30px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 8px;
        cursor: pointer;
        z-index: 99;
        transition: all 0.3s ease;
    `;
    
    document.body.appendChild(button);
    
    button.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        localStorage.setItem('admin-dark-mode', isDark);
        button.innerHTML = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
    });
    
    // Restore dark mode preference
    if (localStorage.getItem('admin-dark-mode') === 'true') {
        document.body.classList.add('dark-mode');
        button.innerHTML = '☀️ Light Mode';
    }
}

// ========= FORM VALIDATION =========
function enhanceFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.style.borderColor = '#ff6b6b';
                    input.style.boxShadow = '0 0 0 3px rgba(255, 107, 107, 0.1)';
                    isValid = false;
                } else {
                    input.style.borderColor = '';
                    input.style.boxShadow = '';
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields');
            }
        });
    });
}

// ========= UTILITY FUNCTIONS =========
function hideSection(sectionName) {
    const sections = document.querySelectorAll('.admin-section');
    sections.forEach(section => {
        const header = section.querySelector('.admin-section-header');
        if (header && header.textContent.includes(sectionName)) {
            section.classList.add('collapsed');
        }
    });
}

function showSection(sectionName) {
    const sections = document.querySelectorAll('.admin-section');
    sections.forEach(section => {
        const header = section.querySelector('.admin-section-header');
        if (header && header.textContent.includes(sectionName)) {
            section.classList.remove('collapsed');
        }
    });
}

// Initialize on page load
window.addEventListener('load', function() {
    makeFieldsetsCollapsible();
    addDarkModeToggle();
    enhanceFormValidation();
});
