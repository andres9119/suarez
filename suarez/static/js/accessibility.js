(function () {
    // Configuration
    const STORAGE_KEY = 'suarez_accessibility_config';

    // Default State
    let state = {
        textLarge: false,
        highContrast: false,
        darkMode: false,
        grayscale: false,
        readableFont: false,
        highlightLinks: false
    };

    // Load State
    function loadState() {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {
            state = JSON.parse(saved);
            applyState();
        }
    }

    // Save State
    function saveState() {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    }

    // Apply State to Body
    function applyState() {
        const body = document.body;

        // Text Large
        if (state.textLarge) body.classList.add('acc-text-large');
        else body.classList.remove('acc-text-large');

        // High Contrast
        if (state.highContrast) {
            body.classList.add('acc-high-contrast');
            // Disable Dark Mode if High Contrast is on
            state.darkMode = false;
            body.classList.remove('acc-dark-mode');
        } else {
            body.classList.remove('acc-high-contrast');
        }

        // Dark Mode
        if (state.darkMode) {
            body.classList.add('acc-dark-mode');
            // Disable High Contrast if Dark Mode is on
            state.highContrast = false;
            body.classList.remove('acc-high-contrast');
        } else {
            body.classList.remove('acc-dark-mode');
        }

        // Grayscale
        if (state.grayscale) body.classList.add('acc-grayscale');
        else body.classList.remove('acc-grayscale');

        // Readable Font
        if (state.readableFont) body.classList.add('acc-readable-font');
        else body.classList.remove('acc-readable-font');

        // Highlight Links
        if (state.highlightLinks) body.classList.add('acc-links');
        else body.classList.remove('acc-links');

        updateButtonStates();
    }

    // Create Widget HTML
    function createWidget() {
        const widgetHTML = `
            <div id="acc-widget-container">
                <button id="acc-widget-btn" aria-label="Opciones de Accesibilidad" title="Accesibilidad">
                    <svg viewBox="0 0 24 24">
                        <path d="M12 2c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm9 7h-6v13h-2v-6h-2v6H9V9H3V7h18v2z"/>
                    </svg>
                </button>
                <div id="acc-panel">
                    <div class="acc-panel-header">
                        <h2 class="acc-panel-title">Accesibilidad</h2>
                        <button class="acc-close-btn" aria-label="Cerrar panel">&times;</button>
                    </div>
                    <div class="acc-options">
                        <button class="acc-option-btn" id="btn-text-large">
                            <span class="acc-icon">A+</span> Aumentar Texto
                        </button>
                        <button class="acc-option-btn" id="btn-dark-mode">
                            <span class="acc-icon">🌙</span> Modo Oscuro
                        </button>
                        <button class="acc-option-btn" id="btn-high-contrast">
                            <span class="acc-icon">◑</span> Alto Contraste
                        </button>
                        <button class="acc-option-btn" id="btn-grayscale">
                            <span class="acc-icon">G</span> Escala de Grises
                        </button>
                        <button class="acc-option-btn" id="btn-readable-font">
                            <span class="acc-icon">F</span> Fuente Legible
                        </button>
                        <button class="acc-option-btn" id="btn-links">
                            <span class="acc-icon">🔗</span> Resaltar Enlaces
                        </button>
                    </div>
                    <button class="acc-reset-btn" id="btn-reset">Restablecer Todo</button>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', widgetHTML);
    }

    // Event Listeners
    function setupEventListeners() {
        const btn = document.getElementById('acc-widget-btn');
        const panel = document.getElementById('acc-panel');
        const closeBtn = document.querySelector('.acc-close-btn');

        // Toggle Panel
        btn.addEventListener('click', () => {
            panel.classList.toggle('visible');
        });

        closeBtn.addEventListener('click', () => {
            panel.classList.remove('visible');
        });

        // Options
        document.getElementById('btn-text-large').addEventListener('click', () => {
            state.textLarge = !state.textLarge;
            applyAndSave();
        });

        document.getElementById('btn-dark-mode').addEventListener('click', () => {
            state.darkMode = !state.darkMode;
            // High contrast and dark mode are mutually exclusive
            if (state.darkMode) state.highContrast = false;
            applyAndSave();
        });

        document.getElementById('btn-high-contrast').addEventListener('click', () => {
            state.highContrast = !state.highContrast;
            // High contrast and dark mode are mutually exclusive
            if (state.highContrast) state.darkMode = false;
            applyAndSave();
        });

        document.getElementById('btn-grayscale').addEventListener('click', () => {
            state.grayscale = !state.grayscale;
            applyAndSave();
        });

        document.getElementById('btn-readable-font').addEventListener('click', () => {
            state.readableFont = !state.readableFont;
            applyAndSave();
        });

        document.getElementById('btn-links').addEventListener('click', () => {
            state.highlightLinks = !state.highlightLinks;
            applyAndSave();
        });

        // Reset
        document.getElementById('btn-reset').addEventListener('click', () => {
            state = {
                textLarge: false,
                highContrast: false,
                darkMode: false,
                grayscale: false,
                readableFont: false,
                highlightLinks: false
            };
            applyAndSave();
        });
    }

    function applyAndSave() {
        applyState();
        saveState();
    }

    function updateButtonStates() {
        document.getElementById('btn-text-large').classList.toggle('active', state.textLarge);
        document.getElementById('btn-high-contrast').classList.toggle('active', state.highContrast);
        document.getElementById('btn-dark-mode').classList.toggle('active', state.darkMode);
        document.getElementById('btn-grayscale').classList.toggle('active', state.grayscale);
        document.getElementById('btn-readable-font').classList.toggle('active', state.readableFont);
        document.getElementById('btn-links').classList.toggle('active', state.highlightLinks);
    }

    let eventListenersSet = false;

    // Initialize
    document.addEventListener('DOMContentLoaded', () => {
        createWidget();

        const btn = document.getElementById('acc-widget-btn');
        btn.addEventListener('click', () => {
            if (!eventListenersSet) {
                setupEventListeners();
                eventListenersSet = true;
                const panel = document.getElementById('acc-panel');
                panel.classList.add('visible');
            } else {
                const panel = document.getElementById('acc-panel');
                panel.classList.toggle('visible');
            }
        });

        loadState();
    });

})();
