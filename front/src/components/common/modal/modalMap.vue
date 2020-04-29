<template>
  <div class="modal-map-wrapper">
    <div class="modal-map-container">
      <button class="modal-map-collide" v-on:click="exitModal">
        <span>✖</span>
      </button>
      <div class="mapapp-container">
        <div id="map" class="kakao-map search-map"></div>
      </div>
    </div>
  </div>
</template>
<script
  type="text/javascript"
  src="//dapi.kakao.com/v2/maps/sdk.js?appkey=69d0c2177d4e8cf1a0f7361daafcc7ac&libraries=services"
></script>
<script>
import axios from "axios";
import { stringify } from "querystring";

export default {
  name: "modalMap",
  components: {},
  data() {
    return {
      address: "",
      isClicked: false,
      btnText: "여기에요!",
      bgColor: "white",
      addinput: "",
    };
  },
  methods: {
    // getXY() {
    //   var componentInstance = this;
    //   axios
    //     .get("https://dapi.kakao.com/v2/local/search/address.json", {
    //       params: {
    //         query: this.address,
    //       },
    //       headers: {
    //         Authorization: "KakaoAK f8d38a34b065785c71e6beed1528657f",
    //       },
    //     })
    //     .then((res) => {
    //       this.addressList = res.data.documents;
    //       var mapContainer = document.getElementById("map"),
    //         mapOption = {
    //           center: new kakao.maps.LatLng(
    //             res.data.documents[0].y,
    //             res.data.documents[0].x
    //           ),
    //           level: 3,
    //         };

    //       var map = new kakao.maps.Map(mapContainer, mapOption);

    //       var marker = new kakao.maps.Marker({
    //         position: map.getCenter(),
    //       });
    //       marker.setMap(map);
    //     })
    //     .catch(() => {
    //       alert("지역명을 입력해주세요.");
    //     });
    // },
    updateAddress() {
      // console.log(this.x, this.y);
    },
    exitModal() {
      this.isClicked = true;
      this.$emit("exit_Clicked", this.isClicked);
    },
  },
  computed: {
    locX() {
      return this.$store.state.locationX;
    },
    locY() {
      return this.$store.state.locationY;
    },
  },
  mounted() {
    var mapContainer = document.getElementById("map"), // 지도를 표시할 div
      mapOption = {
        center: new kakao.maps.LatLng(this.locY, this.locX), // 지도의 중심좌표
        level: 3, // 지도의 확대 레벨
      };

    // 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
    var map = new kakao.maps.Map(mapContainer, mapOption);
    var marker = new kakao.maps.Marker({
      // 지도 중심좌표에 마커를 생성합니다
      position: map.getCenter(),
    });

    marker.setMap(map);
    kakao.maps.event.addListener(map, "click", function(mouseEvent) {
      var latlng = mouseEvent.latLng;
      marker.setPosition(latlng);
      this.x = latlng.getLng();
      this.y = latlng.getLat();
    });
  },
};
</script>
<style scoped>
.mapapp-container {
  top: 0;
  left: 0;
  position: relative;
  text-align: center;
}
.search-map {
  position: relative;
  width: 100%;
  height: 40vh;
  margin-bottom: 20px;
}

.modal-map-wrapper {
  /* position */
  position: fixed;
  top: 32%;
  right: 5%;

  /* modal shape */
  height: 40%;
  width: 20%;
  border: 1px solid black;
  /* border-radius: 15px; */

  /* content */
  background-color: ghostwhite;
  color: black;
  font-size: 1rem;
}

.modal-map-container {
  width: 100%;
  height: 100%;
}

.modal-map-collide {
  position: absolute;
  top: 0;
  right: 0;
  border: none;
  background: transparent;
  font-size: 40px;
  z-index: 10;
}
</style>
