<script>
function encryptImage() {
    const fileInput = document.getElementById("image");
    const file = fileInput.files[0];
    if (!file) {
        alert("Please select an image file.");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    fetch("/encrypt", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Encryption failed.");
        }
        return response.blob();
    })
    .then(blob => {
        const downloadLink = document.getElementById("downloadLink");
        const imageURL = URL.createObjectURL(blob);
        downloadLink.href = imageURL;
        downloadLink.style.display = "block";
    })
    .catch(error => {
        console.error("Encryption error:", error);
        alert("Encryption failed. Please try again.");
    });
}
</script>
