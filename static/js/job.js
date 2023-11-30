document.addEventListener('DOMContentLoaded', function () {
    const jobButtons = document.querySelectorAll('.job__title');

    jobButtons.forEach(button => {
        button.addEventListener('click', function () {
            const jobId = this.getAttribute('data-job-id');
            const content = document.querySelector(`.job__wrapper-info[data-job-id="${jobId}"]`);

            content.classList.toggle('jobb-content');

            const arrowIcon = this.querySelector('img');
            arrowIcon.classList.toggle('rotate-90');
        });
    });
});
