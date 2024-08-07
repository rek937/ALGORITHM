/* 🚀🔥
黃綠紅 你要哪一個？

此專案涵蓋的概念
- DOM 操作
- 事件監聽器
- 迴圈 forEach 
- 變數
- 條件語句 (if else if)
- 樣板字面值
*/


// // 將 title 文字改成 '報告阿柴，標題已經切換！' 並將字體顏色改成藍色
// function changeTitle(){
//   let titleDiv = document.getElementById('title')
//   console.log("title", titleDiv)
//   let msgs = "The title has been changed!"
//   titleDiv.innerText = msgs
// }

const squares = document.querySelectorAll('.colorSquare')
const output = document.getElementById("output")

// 將每個元素綁定
squares.forEach(square => {
  square.onclick = () => {
    _id = square.getAttribute("id")
    console.log("id", _id)
    output.innerHTML = `<div class='colorSquare id="${_id}" > </div>`
  }
})

// function resetScore() {

// }

// const resetGameBtn = document.getElementById('reset')
// // 綁定 reset 事件
// resetGameBtn.onclick = () => resetScore()

