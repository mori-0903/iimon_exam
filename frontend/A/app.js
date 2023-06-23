// APIのURL
const apiUrl = 'https://catfact.ninja/fact';

// DOM要素の取得
const getFactBtn = document.getElementById('get-fact-btn');
const factText = document.getElementById('fact-text');
// ボタンがクリックされたときの処理
getFactBtn.addEventListener('click', () => {
  // APIリクエストの送信
  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      // 取得したデータの表示
      factText.textContent = data.fact;
    })
    .catch(error => {
      // エラーメッセージの表示
      factText.textContent = 'An error occurred while fetching the cat fact.';
      console.error(error);
    });
});

