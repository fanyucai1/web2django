function setupProgressHandling() {
    const form = document.querySelector('form');
    const fileInput = document.querySelector('input[type="file"]');
    if (form && fileInput) {
        form.addEventListener('submit', function (event) {
            event.preventDefault();
            const formData = new FormData(form);
            const xhr = new XMLHttpRequest();
            xhr.open('POST', form.action, true);

            // 进度条事件监听
            xhr.upload.onprogress = function (e) {
                if (e.lengthComputable) {
                    const percentage = (e.loaded / e.total) * 100;
                    console.log(percentage + '%');
                    // 更新进度条的代码
                }
            };

            xhr.onload = function () {
                if (xhr.status === 200) {
                    console.log('上传成功');
                } else {
                    console.error('上传失败');
                }
            };

            xhr.send(formData);
        });
    }
}