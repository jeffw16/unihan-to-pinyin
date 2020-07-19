let page = document.getElementById('buttonDiv');
function constructOptions() {
    let button = document.createElement('button');
    button.innerHTML = "Pinyin only";
    
    button.addEventListener('click', function() {
        chrome.storage.sync.set({mode: 0}, function() {
            console.log('Mode is pinyin only');
        })
    });
    page.appendChild(button);

    let button2 = document.createElement('button');
    button2.innerHTML = "Chinese only";
    
    button2.addEventListener('click', function() {
        chrome.storage.sync.set({mode: 1}, function() {
            console.log('Mode is Chinese only');
        })
    });
    page.appendChild(button2);

    let button3 = document.createElement('button');
    button3.innerHTML = "Chinese + pinyin";
    
    button3.addEventListener('click', function() {
        chrome.storage.sync.set({mode: 2}, function() {
            console.log('Mode is Chinese + pinyin');
        })
    });
    page.appendChild(button3);
}
constructOptions();