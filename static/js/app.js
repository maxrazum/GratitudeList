// Build the nav
const sections = document.querySelectorAll('section');
const fragment = document.createDocumentFragment();

for (section of sections) {
    let newElement = document.createElement('li');
    newElement.innerHTML = `<a href="#${section.id}" class="menu__link">${section.dataset.nav}</a>`;

    fragment.appendChild(newElement);
}

document.querySelector('.navbar__menu').appendChild(fragment);

// Scroll to anchor ID using scrollTO event
const navBar = document.querySelector('.navbar__menu');

function scroll(event) {
    event.preventDefault();
    let section = document.querySelector(event.target.hash);
    scrollTo( {
        top: section.offsetTop - 100,
        behavior: 'smooth'
    });
}

navBar.addEventListener('click', scroll);