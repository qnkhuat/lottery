document.addEventListener('DOMContentLoaded',()=>{

  document.querySelector('#form').onsubmit = () => {
    const request = new XMLHttpRequest();
    const currency = document.querySelector('#currency').value;
    request.open('POST','/ajax');
    request.onload = () => {
      const data = JSON.parse(request.responseText);
      if (data.success){
        const contents = `1 USD is equal to ${data.md5}`;
        document.querySelector('#result').innerHTML = contents;
      }else {
        document.querySelector('#result').innerHTML = "Error";
      }
    }

    const data = new FormData();
    data.append('currency',currency);
    request.send(data);
    return false;
  }


})
