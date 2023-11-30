// job.js
document.addEventListener('DOMContentLoaded', function () {
    const jobButtons = document.querySelectorAll('.job__title');

    jobButtons.forEach(button => {
        button.addEventListener('click', function () {
            const content = this.nextElementSibling;
            content.classList.toggle('jobb-content-show');

            const arrowIcon = this.querySelector('img');
            arrowIcon.classList.toggle('rotate-90');
        });
    });
});
