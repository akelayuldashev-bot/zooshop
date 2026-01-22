document.addEventListener("DOMContentLoaded", () => {

    /* ================= ENTRANCE ANIMATION ================= */
    const cards = document.querySelectorAll(".favorite-card-dark");

    cards.forEach((card, i) => {
        setTimeout(() => {
            card.classList.add("show");
        }, i * 120);
    });

    /* ================= HEART PARTICLES ================= */
    document.querySelectorAll(".favorite-remove").forEach(btn => {
        btn.addEventListener("click", e => {
            e.preventDefault();

            const card = btn.closest(".favorite-card-dark");

            // Heart particles
            for (let i = 0; i < 8; i++) {
                const particle = document.createElement("span");
                particle.innerHTML = "❤";
                particle.classList.add("heart-particle");

                const x = Math.random() * 60 - 30;
                const y = Math.random() * -60 - 20;

                particle.style.setProperty("--x", `${x}px`);
                particle.style.setProperty("--y", `${y}px`);

                btn.appendChild(particle);

                setTimeout(() => particle.remove(), 900);
            }

            // Collapse animation
            card.style.transition = "all 0.5s ease";
            card.style.transform = "scale(0.9)";
            card.style.opacity = "0";

            setTimeout(() => {
                window.location.href = btn.href;
            }, 450);
        });
    });

});
