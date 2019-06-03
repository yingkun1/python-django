function News() {

}

News.prototype.initUEditor = function(){
    window.ue = UE.getEditor('editor',{
        'initialFrameHeight':400,
        'serverUrl':'/ueditor/upload/',

    });

};

News.prototype.listenUploadFileEvent = function(){
    var uploadBtn = $('#thumbnail-btn');
    uploadBtn.change(function () {
        var file = uploadBtn[0].files[0];
        var formData = new FormData();
        formData.append('file',file);
        xfzajax.post({
           'url':'/cms/upload_file/',
            'data':formData,
            'processData':false,
            'contentType':false,
            'success':function (result) {
                if(result['code'] === 200){
                    var url = result['data']['url'];
                    var thumbnailInput = $("#thumbnail-form");
                    thumbnailInput.val(url);
                }
            }
        });
    });
};

//上传文件到七牛云
News.prototype.listenQiniuUploadFileEvent = function(){
    var self = this;
    var uploadBtn = $('#thumbnail-btn');
    uploadBtn.change(function () {
        var file = this.files[0];
        xfzajax.get({
            'url':'/cms/qntoken/',
            'success':function (result) {
                if(result['code'] === 200){
                    var token = result['data']['token'];
                    var key = (new Data()).getTime() + '.' + file.name.split('.')[1];
                    var putExtra = {
                        fname : key,
                        params : {},
                        mimeType:['image/png','image/jpeg','image/gif']
                    };
                    var config = {
                        useCdnDomain:true,
                        retryCount:6,
                        region:qiniu.region.z0              //华东地区
                    };
                    var observable = qiniu.upload(file,key,token,putExtra,config);
                    observable.subscribe({
                        'next': self.handleFileUploadProgress,
                        'error': self.handleFileUploadError,
                        'complete': self.handleFileUploadComplete,
                    });
                }
            }
        })
    });
};

//处理文件上传的过程
News.prototype.handleFileUploadProgress = function(response){
      var total = response.total;
      var percent = total.percent;
      var percentText = percent.toFixed(0)+"%";
      // console.log(percent);
      // var progressGroup = News.progressGroup;
      progressGroup.show();
      var progressBar = $(".progress-bar");
      progressBar.css({"width":percentText});
      progressBar.text(percentText);

};

//上传过程中发生错误
News.prototype.handleFileUploadError = function(error){
    window.messageBox.showError(error.message);
    var progressGroup = $("#progress-group");
    progressGroup.hide();
    console.log(error.message);

};

//文件上传完成后执行的回调函数
News.prototype.handleFileUploadComplete = function(response){
      console.log(response);
      var progressGroup = $("#progress-group");
      progressGroup.hide();
      var domain = 'http://7xqenu.com1.z0.glb.clouddn.com/';
      var filename = response.key;
      var url = domain+filename;
      var thumbnailInput = $("#thumbnail-form");
      thumbnailInput.val(url);

};

News.prototype.listenSubmitEvent = function(){
    var submitBtn = $("#submit-btn1");
    submitBtn.click(function (event) {
        event.preventDefault();
        var btn = $(this);
        var pk = btn.attr('data-news-id');

        var title = $("input[name='title']").val();
        var category = $("select[name='category']").val();
        var desc = $("input[name='desc']").val();
        var thumbnail = $("input[name='thumbnail']").val();
        var content = window.ue.getContent();
        var url = '';
        if(pk){
            url = '/cms/edit_news/';
        }else{
            url = '/cms/write_news/';
        }

        xfzajax.post({
            'url':url,
            'data':{
                'title':title,
                'category':category,
                'desc':desc,
                'thumbnail':thumbnail,
                'content':content,
                'pk':pk,
            },
            'success':function (result) {
                if (result['code'] === 200){
                    xfzalert.alertSuccess('恭喜!新闻发表成功!',function () {
                       window.location.reload();
                    });

                }
            }
        });
    });
};

News.prototype.run = function () {
    var self = this;
    self.initUEditor();
    self.listenUploadFileEvent();
    self.listenSubmitEvent();
    // self.listenQiniuUploadFileEvent();
};

$(function () {
    var news = new News();
    news.run();
    // News.progressGroup = $('#progress-group');
});