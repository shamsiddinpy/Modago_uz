document.addEventListener('DOMContentLoaded', function () {
    // Clear input functionality
    document.querySelectorAll('.clear-input').forEach(button => {
        button.addEventListener('click', function () {
            const input = this.previousElementSibling;
            input.value = '';
            input.focus();
        });
    });

    // Character counter for editor
    const editor = document.querySelector('.editor-content');
    const charCount = document.querySelector('.char-count');

    editor.addEventListener('input', function () {
        const length = this.textContent.length;
        charCount.textContent = `${length}/4096`;
    });

    // File upload handling
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');

    dropZone.addEventListener('click', () => fileInput.click());

    fileInput.addEventListener('change', function (e) {
        if (e.target.files && e.target.files[0]) {
            // Handle file upload here
            const file = e.target.files[0];
            console.log('Selected file:', file);
        }
    });

    // Form submission
    document.getElementById('categoryForm').addEventListener('submit', function (e) {
        e.preventDefault();
        // Handle form submission here
        console.log('Form submitted');
    });

    // Text editor toolbar functionality
    document.querySelectorAll('.editor-toolbar button').forEach(button => {
        button.addEventListener('click', function () {
            const command = this.title.toLowerCase();
            if (command === 'link') {
                const url = prompt('Enter URL:');
                if (url) document.execCommand('createLink', false, url);
            } else {
                document.execCommand(command, false, null);
            }
            editor.focus();
        });
    });
});

// Search functionality
const searchInput = document.querySelector('.search-input');
const tableRows = document.querySelectorAll('tbody tr');

searchInput.addEventListener('input', function (e) {
    const searchTerm = e.target.value.toLowerCase();

    tableRows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(searchTerm) ? '' : 'none';
    });
});

// Toggle switches
document.querySelectorAll('.switch input').forEach(toggle => {
    toggle.addEventListener('change', function () {
        console.log('Toggle state changed:', this.checked);
        // Add your toggle handling logic here
    });
});

// Action buttons
document.querySelectorAll('.action-btn').forEach(btn => {
    btn.addEventListener('click', function () {
        const action = this.getAttribute('title');
        console.log('Action clicked:', action);
        // Add your action handling logic here
    });
});

// Create button
document.querySelector('.btn-create').addEventListener('click', function () {
    console.log('Create button clicked');
    // Add your create handling logic here
});

// Import button
document.querySelector('.btn-import').addEventListener('click', function () {
    console.log('Import button clicked');
    // Add your import handling logic here
});

// Basic drag and drop functionality
let draggedItem = null;

document.querySelectorAll('.drag-handle').forEach(handle => {
    const row = handle.closest('tr');

    handle.addEventListener('dragstart', function () {
        draggedItem = row;
        setTimeout(() => row.style.opacity = '0.5', 0);
    });

    handle.addEventListener('dragend', function () {
        draggedItem = null;
        row.style.opacity = '';
    });

    row.addEventListener('dragover', function (e) {
        e.preventDefault();
    });

    row.addEventListener('drop', function (e) {
        e.preventDefault();
        if (draggedItem && draggedItem !== row) {
            const allRows = [...row.parentNode.children];
            const draggedPos = allRows.indexOf(draggedItem);
            const droppedPos = allRows.indexOf(row);

            if (draggedPos < droppedPos) {
                row.parentNode.insertBefore(draggedItem, row.nextSibling);
            } else {
                row.parentNode.insertBefore(draggedItem, row);
            }
        }
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const createButton = document.getElementById('createButton');
    const modal = document.getElementById('categoryModal');
    const modalClose = document.querySelector('.modal-close');
    const cancelButton = document.querySelector('.btn-cancel');
    modal.style.display = 'none';

    // Modal oynani markazlashtirish
    function centerModal() {
        modal.style.display = 'flex';  // Display modal as a flexbox
        modal.style.justifyContent = 'center';
        modal.style.alignItems = 'center';
    }


    // "Yaratish" tugmasi bosilganda modal oynani ko'rsatish
    createButton.addEventListener('click', function () {
        centerModal();  // Markazlashtirish funksiyasini chaqiramiz
    });

    // Modal oynani yopish
    modalClose.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    cancelButton.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    // Modal oynasini tashqi qismini bosganda yopish
    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});

