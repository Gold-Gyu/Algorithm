// 비동기에서도 순서를 보장해준다

// 콜백함수 or Promise

// 나는 물 => 스프 => 면 순서대로 하고 싶다.

console.log("라면을 끓이자(각 재료가 준비되는데 1~3초 시간이 걸린다)")

// 라면 = 물, 스프, 면
let aFinished = false; // 물
let bFinished = false; // 스프
let cFinished = false; // 면


// call back 함수
setTimeout(() => {
    console.log("A: 물을 넣는다")
    setTimeout(() => {
        console.log("B: 스프을 넣는다")
        setTimeout(() => {
            console.log("C: 면을 넣는다")
            console.log("라면을 끓인다")
        }, Math.random() * 2000 + 1000);
    }, Math.random() * 2000 + 1000)
}, Math.random() * 2000 + 1000);


// Promise
