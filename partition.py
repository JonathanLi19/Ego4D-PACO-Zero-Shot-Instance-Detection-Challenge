import json
def main():
    with open("/home/liujinfan/workspace/paco/datasets/paco/annotations/paco_ego4d_v1_test.json",'r') as load_f:
        load_dict = json.load(load_f)
    ann = load_dict['annotations']
    image_bboxs = {}
    # image_category = {}
    for item in ann:
        image_id = item['image_id']
        bbox = item['bbox']
        # category_id = item['category_id']
        if image_id in image_bboxs.keys():
            image_bboxs[image_id].append(bbox)
        else:
            image_bboxs[image_id] = [bbox]
        # if image_id in image_category.keys():
        #     image_category[image_id].append(category_id)
        # else:
        #     image_category[image_id] = [category_id]
    with open("/home/liujinfan/workspace/paco/datasets/paco/annotations/paco_ego4d_v1_test_bboxs_partition.json","w") as f:
        json.dump(image_bboxs,f)
    print("OK!!!")
    return
if __name__ == '__main__':
    main()
