const storedTheme = localStorage.getItem('theme')

const getPreferredTheme = () => {
    if (storedTheme) {
        return storedTheme
    }

    return 'auto'
}

const setTheme = function (theme) {
    if (theme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-bs-theme', 'dark')
        localStorage.setItem('theme', theme)

    } else {
        document.documentElement.setAttribute('data-bs-theme', theme)
        localStorage.setItem('theme', theme)
    }
}

setTheme(getPreferredTheme())
