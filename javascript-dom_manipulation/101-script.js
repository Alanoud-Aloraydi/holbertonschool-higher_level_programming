document.addEventListener('DOMContentLoaded', () => {
  const languageCode = document.querySelector('#language_code');
  const translateButton = document.querySelector('#btn_translate');
  const hello = document.querySelector('#hello');

  translateButton.addEventListener('click', () => {
    const language = encodeURIComponent(languageCode.value);

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${language}`)
      .then(response => response.json())
      .then(data => {
        hello.textContent = data.hello;
      })
      .catch(error => console.error('Unable to fetch translation:', error));
  });
});
