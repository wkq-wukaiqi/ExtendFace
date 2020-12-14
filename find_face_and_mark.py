import face_recognition
import os
from PIL import Image
import sys
import matplotlib.image as mat_img
import matplotlib.pyplot as plt
import re





if __name__ == '__main__':
    # 图片文件根路径
    img_root_path='./web_face_img/'
    # 人脸输出文件夹
    img_dest_path='./face_img/'
    #打分文件
    face_score_path='./scores.txt'
    if not os.path.exists(img_dest_path):
        os.mkdir(img_dest_path)
        #获取所有图片文件
        img_list=os.listdir(img_root_path)
        print('发现了'+str(len(img_list))+'张图片')
        i=1
        for img in img_list:
            print('\r',end='')
            sys.stdout.write('正在提取第{}张图片的人脸'.format(i))
            image=face_recognition.load_image_file(img_root_path+img)
            face_locations=face_recognition.face_locations(image)
            for face_location in face_locations:
                #人脸在图片中的坐标
                top,right,bottom,left=face_location
                #扩大一点范围
                top=int(top*0.9)
                right=int(right*1.1)
                bottom=int(bottom*1.1)
                left=int(left*0.9)
                face_image=image[top:bottom,left:right]
                pil_image=Image.fromarray(face_image)
                pil_image.save(img_dest_path+img)
            i+=1
            sys.stdout.flush()
    print('人脸提取完毕！')
    #打开人脸文件打分
    if not os.path.exists(face_score_path):
        score_file=open(face_score_path,'w')
    else:
        score_file=open(face_score_path,'r+')
    if score_file:
        #获取已打分的文件名
        done=score_file.readlines()
        done_list=[]
        for done_name in done:
            done_list.append(done_name.split('-')[0])
        for face_file_name in os.listdir(img_dest_path):
            #已打分的就跳过
            if not face_file_name in done_list:
                #读取并展示图片
                face_img=mat_img.imread(img_dest_path+face_file_name)
                plt.imshow(face_img)
                plt.axis('off')
                flag=False
                exit=False
                print('请输入该人脸的分数，范围是1-9的整数。如果人脸不是中国人、模糊、角度不对，输入0舍弃，输入-1结束打分:', end='')
                plt.show()
                #检查输入
                while not flag:
                    score_str=input()
                    if not re.match(r'^(-1)|\d{1}$',score_str):
                        print('输入格式错误，请重新输入:',end='')
                        continue
                    else:
                        if score_str=='-1':
                            exit=True
                            break
                        flag=True
                        score_file.write(face_file_name+'-'+score_str+'\n')
                if exit==True:
                    break
        score_file.close()
        print('打分完毕！')
    else:
        print('文件打开失败！')



