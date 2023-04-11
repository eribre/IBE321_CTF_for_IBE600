/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */

// New version that uses 'this' to target the clicked element
var myFunction = function (target) {
    if (
        target.parentNode.querySelector(".dropdown-content").style.display ==
        "none"
    ) {
        target.parentNode.querySelector(".dropdown-content").style.display =
            "block";
        target.parentNode.querySelector(".rotate").classList.add("down");
    } else {
        target.parentNode.querySelector(".dropdown-content").style.display =
            "none";
        target.parentNode.querySelector(".rotate").classList.remove("down");
    }
};

// Separate event listeners for each dropdown menu
// SQL injection dropdown
window.addEventListener("click", function (e1) {
    if (!e1.target.matches(".dropbtn")) {
        document.getElementById("drop_content_1").style.display = "none";
        document.getElementById("rotate_1").classList.remove("down");
    }
});

// Cryptography dropdown
window.addEventListener("click", function (e2) {
    if (!e2.target.matches(".dropbtn")) {
        document.getElementById("drop_content_2").style.display = "none";
        document.getElementById("rotate_2").classList.remove("down");
    }
});

// Old version kept for reference/learning purposes

// Old js version
/*
function toggleDrop() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (e) {
    if (!e.target.matches(".dropbtn")) {
        var myDropdown = document.getElementById("myDropdown");
        if (myDropdown.classList.contains("show")) {
            myDropdown.classList.remove("show");
        }
    }
};
*/

/* Slighlt less old js version
document.addEventListener("DOMContentLoaded", function () {
    // Dropdown menu script
    document.querySelector(".dropbtn").onclick = function () {
        if (
            document.querySelector(".dropdown-content").style.display == "none"
        ) {
            document.querySelector(".dropdown-content").style.display = "block";
            document.querySelector(".rotate").classList.add("down");
        } else {
            document.querySelector(".dropdown-content").style.display = "none";
            document.querySelector(".rotate").classList.remove("down");
        }
    };
    // Close the dropdown if the user clicks outside of it
    window.onclick = function (e) {
        if (!e.target.matches(".dropbtn")) {
            document.querySelector(".dropdown-content").style.display = "none";
            document.querySelector(".rotate").classList.remove("down");
        }
    };
});
*/

// jquery version (old)
/*
$(document).ready(function () {
    $(".dropbtn").click(function () {
        $(".dropdown-content").toggle();
        if ($(".dropdown-content").is(":visible")) {
            $(".rotate").addClass("down");
        } else if ($(".dropdown-content").is(":hidden")) {
            $(".rotate").removeClass("down");
        }
    });
    $(window).click(function (e) {
        if (!$(e.target).is(".dropbtn")) {
            $(".dropdown-content").hide();
            if ($(".dropdown-content").is(":hidden")) {
                $(".rotate").removeClass("down");
            }
        }
    });
});
*/
