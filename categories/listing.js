const tabs = document.querySelectorAll('[data-tab-target]')
const tabContents = document.querySelectorAll('[data-tab-content]')

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.tabTarget)
        tabContents.forEach(tabContent => {
            tabContent.classList.remove('tabactive')
        })
        tabs.forEach(tab => {
            tab.classList.remove('tabactive')
        })
        tab.classList.add('tabactive')
        target.classList.add('tabactive')
    })
});