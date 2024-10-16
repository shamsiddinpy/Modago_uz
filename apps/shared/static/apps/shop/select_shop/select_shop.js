document.addEventListener('DOMContentLoaded', function () {
    const selectedLanguages = document.getElementById('selected-languages');
    const languageDropdown = document.getElementById('language-dropdown');
    const languageSelect = document.getElementById('language');

    selectedLanguages.addEventListener('click', function () {
        languageDropdown.classList.toggle('show');
    });

    languageDropdown.addEventListener('change', function (e) {
        if (e.target.type === 'checkbox') {
            updateSelectedLanguages();
        }
    });

    function updateSelectedLanguages() {
        const checkboxes = languageDropdown.querySelectorAll('input[type="checkbox"]:checked');
        selectedLanguages.innerHTML = '';

        if (checkboxes.length === 0) {
            selectedLanguages.innerHTML = '<span class="text-muted">Tillarni tanlang</span>';
        } else {
            checkboxes.forEach(checkbox => {
                const badge = document.createElement('span');
                badge.classList.add('badge', 'bg-primary', 'me-1', 'mb-1');
                badge.textContent = checkbox.parentElement.textContent.trim();

                const removeBtn = document.createElement('button');
                removeBtn.type = 'button';
                removeBtn.classList.add('btn-close', 'btn-close-white', 'ms-1');
                removeBtn.style.fontSize = '0.65em';
                removeBtn.addEventListener('click', function (e) {
                    e.stopPropagation();
                    checkbox.checked = false;
                    updateSelectedLanguages();
                });

                badge.appendChild(removeBtn);
                selectedLanguages.appendChild(badge);
            });
        }

        // Update the hidden select element
        Array.from(languageSelect.options).forEach(option => {
            option.selected = Array.from(checkboxes).some(cb => cb.value === option.value);
        });
    }

    // Close dropdown when clicking outside
    document.addEventListener('click', function (e) {
        if (!selectedLanguages.contains(e.target) && !languageDropdown.contains(e.target)) {
            languageDropdown.classList.remove('show');
        }
    });
});


function clearInput(inputId) {
    document.getElementById(inputId).value = '';
}

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('storeCreationForm');
    form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add('was-validated');
    });
});

