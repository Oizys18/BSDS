<template>
  <div>
    <paginated-list :pageHead="'작성한 글 목록'" :items="items" :itemHeader="itemHeader"/>
  </div>
</template>

<script>
import paginatedList from "@/views/admin/components/paginatedList";
export default {
  name: "createdList",
  components: {
    paginatedList
  },
  data() {
    return {
      itemHeader: ["관리번호", "사진", "분류", "등록일", "조회"],
      items: [{
          "id": 1,
          "image": "imageUrl",
          "category": "createdList",
          "date": "2020-04-25",
        }, {
          "id": 2,
          "image": "imageUrl",
          "category": "createdList",
          "date": "2020-04-25",
        }, {
          "id": 3,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
        }, {
          "id": 4,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
        }, {
          "id": 5,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
        }, {
          "id": 6,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
        }, {
          "id": 7,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
        }, {
          "id": 8,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
        }, {
          "id": 9,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
        }, {
          "id": 10,
          "image": "imageUrl",
          "category": "분류..뭐",
          "date": "2020-04-25",
      }]
    }
  }
}
</script>

<style scoped>

</style>