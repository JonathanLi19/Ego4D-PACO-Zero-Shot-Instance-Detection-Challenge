import json
def main():
    with open("/home/liujinfan/workspace/paco/datasets/paco/annotations/paco_ego4d_v1_test.json",'r') as load_f:
        load_dict = json.load(load_f)
    images = load_dict['images']
    image_size = {}
    # image_category = {}
    for item in images:
        image_id = item['id']
        width = item['width']
        height = item['height']
        # category_id = item['category_id']
        image_size[image_id] = [height, width]
        # if image_id in image_category.keys():
        #     image_category[image_id].append(category_id)
        # else:
        #     image_category[image_id] = [category_id]
    with open("/home/liujinfan/workspace/paco/datasets/paco/annotations/paco_ego4d_v1_test_image_size.json","w") as f:
        json.dump(image_size,f)
    print("OK!!!")
    return
if __name__ == '__main__':
    main()
