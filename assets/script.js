document.addEventListener("DOMContentLoaded", () => {
  const fileInput = document.getElementById("fileInput");
  const uploadBtn = document.getElementById("uploadBtn");
  const status = document.getElementById("status");

  uploadBtn.addEventListener("click", () => {
    const file = fileInput.files[0];
    if (!file) {
      status.textContent = "⚠️ Please choose a file first!";
      return;
    }

    const reader = new FileReader();
    reader.onload = async () => {
      try {
        // Send file name and contents to Python
        const result = await window.pywebview.api.upload_file(file.name, reader.result);
        status.textContent = result;
      } catch (err) {
        console.error("Upload failed:", err);
        status.textContent = "❌ Upload failed.";
      }
    };
    reader.readAsText(file); // for text files
    // For binary files, use reader.readAsDataURL(file);
  });
});
