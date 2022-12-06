from django.shortcuts import render, redirect
from django.conf import settings
from django.http import FileResponse, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from django.urls import reverse

from . import models
from SDTTool_translate import SDTTool

import os
import hashlib
import sys
import subprocess

global translateFile


def sdttool(request):
    context = {}
    if request.method == "POST":
        selected_type = request.POST.get('selected_type')
        # print("HTML에서 넘어온 selected_type: ", selected_type)

        uploaded_file = request.FILES['uploadedFile']
        file_name = uploaded_file.name
        upload_media_dir = os.path.abspath("media/Uploaded Files")
        result_media_dir = os.path.abspath("media/Result Files")

        file_sha = 'z'

        if os.path.isfile(file_name):
            os.remove(file_name)

        fs = FileSystemStorage(location=upload_media_dir)
        name = fs.save(file_name, uploaded_file)

        fileName = file_name.split('.')[0] + '.xml'
        # 여기에 sdt tool 연결하기

        # upload_media_dir에 (fileName+file_sha)로 저장
        old_file = os.path.join(upload_media_dir, fileName)

        new_file = os.path.join(result_media_dir, fileName)
        # os.rename(old_file, new_file) # upload 폴더에 업로드 한 파일을 result 폴더로 옮겨서 다시 저장함.
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print(":::::::::::::::::::::::::::::  Upload Suc  :::::::::::::::::::::::::::::")
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        # print(old_file)

        context['url'] = upload_media_dir + str(file_sha) + '\\'+fileName
        context['old_file'] = old_file

        translateFile = excuteSDT(old_file, selected_type)
        context['new_file'] = translateFile
        context['new_file_name'] = translateFile.split('/')[-1]
    return render(request, "index.html", context)


def excuteSDT(inputfile, selected_type):
    # print("HTML에서 넘어온 selected_type: ", selected_type)
    # 파일 절대경로에서 파일이름에 해당하는  Origin_Echo.xml 만
    fileName = inputfile.split('\\')[-1]
    fileName = fileName.split('.')[0] + "." + selected_type  # 파일이름 재 정의 .md
    # fileName = "TranslateFile." + selected_type
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(":::::::::::::::::::::::::::::  excute SDT  :::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

    # server
    result_media_dir = os.path.abspath("media/Result Files")
    outfile = result_media_dir.replace("\\", "/")+"/"+fileName

    args = ["infile", inputfile.replace("\\", "/"),
            "outfile", outfile]

    try:
        transfile = SDTTool.main(args[1], args[3])
        print("transfile : ", outfile)
    except:
        print("::::::::::::  Error to SDT Tool  ::::::::::::", flush=True)
        sys.exit(1)

    return outfile


def downloadFile(request):
    if request.method == "POST":
        selected_type = request.POST.get('a000')
        selected_type = selected_type.replace("\\", "/")
        mimetype = "." + selected_type.split('.')[-1]

        file_path = os.path.abspath("media/Result Files")
        file_name = os.path.basename(selected_type)
        fs = FileSystemStorage(file_path)
        result = FileResponse(fs.open(file_name, 'rb'))
        RealResult = file_name
        result['Content-Disposition'] = 'attachment; filename="{}"'.format(
            RealResult)

        # return render(request, "upload-filr.html")
    return result


def file_download(request, new_file):  # 이거 아님
    print(request)
    print(new_file)
    fs = FileSystemStorage()
    filename = os.path.abspath("media/Result Files") + new_file
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf)
            response['Content-Disposition'] = 'attachment; filename='+new_file
            return response
    else:
        print("None")
        return HttpResponseRedirect(reverse('index'))
