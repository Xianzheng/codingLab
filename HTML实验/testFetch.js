const UPDATEDB = () => {
    fetch('http://127.0.0.1:8000/app/updateDB/',{
      method:"GET",
    }).then(res => res.json())
      .then(res => {
        alert('更新成功')
        console.log(res)
        // document.getElementById("updatedb").disabled = true
      })
  }