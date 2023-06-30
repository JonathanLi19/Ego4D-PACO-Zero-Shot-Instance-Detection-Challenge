import json
def main():
    with open("/home/liujinfan/workspace/paco/datasets/paco/annotations/paco_lvis_v1_test.json",'r') as load_f:
        load_dict = json.load(load_f)
    ann = load_dict['annotations']
    for item in ann:
        # if("bbox" not in item.keys()):
        #     print("FALSE!!!\n")
        #     return
        # else:
        #     assert(item["bbox"] != [])
        #     print(item["bbox"])
        if("attribute_ids" not in item.keys()):
            print("FALSE!!!\n")
            return
        else:
            assert(item["attribute_ids"] != [])
            print(item["attribute_ids"])
    print("TRUE!!!\n")
    return
if __name__ == '__main__':
    main()