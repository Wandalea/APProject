document.addEventListener("DOMContentLoaded", function() {
    const form= document.getElementById("crystal_form");

    const nameInput = document.getElementById("name");
    const descriptionInput = document.getElementById("description");
    const imageInput = document.getElementById("image");
    const usesInput = document.getElementById("uses");
    const categoryInput = document.getElementById("category");

    const nameError = document.getElementById("nameError");
    const descriptionError = document.getElementById("descriptionError");
    const imageError = document.getElementById("imageError");
    const usesError = document.getElementById("usesError");
    const categoryError = document.getElementById("categoryError");

    function clearErrors() {
        nameError.textContent = "";
        descriptionError.textContent = "";
        imageError.textContent = "";
        usesError.textContent = "";
        categoryError.textContent = "";

        nameInput.classList.remove("is-invalid");
        descriptionInput.classList.remove("is-invalid");
        imageInput.classList.remove("is-invalid");
        usesInput.classList.remove("is-invalid");
        categoryInput.classList.remove("is-invalid");
    }

    form.addEventListener("submit", function (event) {
        clearErrors();

        let isValid = true;

        const nameValue = nameInput.value.trim();
        const descriptionValue = descriptionInput.value.trim();
        const usesValue = usesInput.value.trim();
        const categoryValue = categoryInput.value.trim();
        const imageFile = imageInput.files[0];

        if (nameValue === "") {
            nameError.textContent = "Crystal name is required.";
            nameInput.classList.add("is-invalid");
            isValid = false;
        } else if (nameValue.length < 2) {
            nameError.textContent = "Crystal name must be at least 2 characters.";
            nameInput.classList.add("is-invalid");
            isValid = false;
        }

        if (descriptionValue.length > 200) {
            descriptionError.textContent = "Description must be 200 characters or less.";
            descriptionInput.classList.add("is-invalid");
            isValid = false;
        }

        if (!imageFile) {
            imageError.textContent = "Please choose an image.";
            imageInput.classList.add("is-invalid");
            isValid = false;
        } else {
            const allowedTypes = ["image/jpeg", "image/png", "image/webp", "image/jpg"];
            if (!allowedTypes.includes(imageFile.type)) {
                imageError.textContent = "Image must be JPG, JPEG, PNG, or WEBP.";
                imageInput.classList.add("is-invalid");
                isValid = false;
            }
        }

        if (usesValue.length > 100) {
            usesError.textContent = "Uses must be 100 characters or less.";
            usesInput.classList.add("is-invalid");
            isValid = false;
        }

        if (categoryValue === "") {
            categoryError.textContent = "Please select a category.";
            categoryInput.classList.add("is-invalid");
            isValid = false;
        }

        if (!isValid) {
            event.preventDefault();
        }
    });
});
