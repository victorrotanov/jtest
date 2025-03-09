document.addEventListener("DOMContentLoaded", function () {
  // Проверяем, какой класс темы активен в админке
  const bodyClass = document.body.classList;
  const isDarkTheme = bodyClass.contains("theme-dark");

  // Настройка TinyMCE в зависимости от темы
  tinymce.init({
    selector: "textarea",
    theme: "silver",
    skin: isDarkTheme ? "oxide-dark" : "oxide", // Используем темную или светлую тему
    plugins:
      "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table contextmenu directionality emoticons paste textcolor",
    toolbar1:
      "undo redo | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image media | forecolor backcolor emoticons",
    branding: false,
  });
});
