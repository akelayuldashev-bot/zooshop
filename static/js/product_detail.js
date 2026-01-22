document.addEventListener("DOMContentLoaded", () => {

    const detail = document.querySelector('.product-detail');
    if (detail) {
        detail.classList.add('show');
    }

    const cartBtn = document.querySelector('.product-btn');
    if (cartBtn) {
        cartBtn.addEventListener('click', () => {
            cartBtn.classList.add('clicked');
            setTimeout(() => {
                cartBtn.classList.remove('clicked');
            }, 400);
        });
    }

    const comments = document.querySelectorAll('.comment-item');
    comments.forEach((comment, index) => {
        setTimeout(() => {
            comment.classList.add('visible');
        }, index * 120);
    });

});

const tilt = document.querySelector('.js-tilt');
if (tilt) {
  const img = tilt.querySelector('img');
  tilt.addEventListener('mousemove', e => {
    const r = tilt.getBoundingClientRect();
    const x = e.clientX - r.left, y = e.clientY - r.top;
    const rx = ((y / r.height) - .5) * -10;
    const ry = ((x / r.width) - .5) * 10;
    img.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg) scale(1.03)`;
    img.style.boxShadow = `0 25px 60px rgba(0,0,0,.25)`;
  });
  tilt.addEventListener('mouseleave', () => {
    img.style.transform = '';
    img.style.boxShadow = '';
  });
}

document.querySelectorAll('.product-btn').forEach(btn=>{
  btn.addEventListener('click', e=>{
    const c = document.createElement('span');
    c.className='ripple';
    const r = btn.getBoundingClientRect();
    c.style.left = (e.clientX - r.left) + 'px';
    c.style.top  = (e.clientY - r.top)  + 'px';
    btn.appendChild(c);
    setTimeout(()=>c.remove(),600);
  });
});

const fav = document.querySelector('.product-btn.favorite');
if (fav){
  fav.addEventListener('click', ()=>{
    fav.classList.add('boom');
    setTimeout(()=>fav.classList.remove('boom'),400);
  });
}

document.querySelectorAll('.comment-item').forEach((el, i) => {
    el.style.opacity = 0;
    el.style.transform = 'translateY(20px)';
    setTimeout(() => {
        el.style.transition = 'all .5s ease';
        el.style.opacity = 1;
        el.style.transform = 'translateY(0)';
    }, i * 120);
});

document.querySelectorAll('.delete-comment-form').forEach(form => {
    form.addEventListener('submit', e => {
        const item = form.closest('.comment-item');
        if (item) {
            item.style.transition = 'all .35s ease';
            item.style.opacity = 0;
            item.style.transform = 'translateX(30px)';
        }
    });
});

