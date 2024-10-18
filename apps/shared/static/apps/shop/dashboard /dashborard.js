document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = themeToggle.querySelector('i');
    let isSidebarCollapsed = false;

    // Theme handling
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        themeIcon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    }

    // Initialize theme from localStorage or default to dark
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);

    // Theme toggle click handler
    themeToggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });

    // Sidebar toggle on double click
    sidebar.addEventListener('dblclick', function () {
        isSidebarCollapsed = !isSidebarCollapsed;
        sidebar.classList.toggle('collapsed', isSidebarCollapsed);
        mainContent.classList.toggle('expanded', isSidebarCollapsed);
    });
});


document.querySelectorAll('.dropdown-toggle').forEach(item => {
    item.addEventListener('click', event => {
        const dropdown = item.nextElementSibling; // Navbatdagi element - ichki ro'yxat
        const contentArea = document.getElementById('content-area'); // Ochiq joy

        // Har bir dropdown ni yopish
        document.querySelectorAll('.dropdown').forEach(d => {
            if (d !== dropdown) {
                d.style.display = 'none'; // Boshqa dropdownlar yopilsin
            }
        });

        // Agar ko'rsatilsa, yashir, aks holda ko'rsat
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';

        // Ochiq joyni ko'rsatish/yopish
        contentArea.style.display = dropdown.style.display === 'block' ? 'block' : 'none';
    });
});

// Boshqa joylarga bosilganda barcha dropdownlarni yopish
document.addEventListener('click', function (event) {
    if (!event.target.closest('.dropdown-toggle')) {
        document.querySelectorAll('.dropdown').forEach(d => {
            d.style.display = 'none'; // Barcha dropdownlarni yopish
        });
        document.getElementById('content-area').style.display = 'none'; // Ochiq joyni yashirish
    }
});

