<template>
  <div class="home">

    <Listing :item="items[2]"/>
    
    <!-- popular campaigns -->
    <section id="popular-campaigns" class="xs-gray-bg waypoint-tigger xs-section-padding">
      <div class="container">
        <div class="xs-section-heading row xs-margin-0">
          <div class="fundpress-heading-title xs-padding-0 col-xl-9 col-md-9">
            <h2 class="color-navy-blue">Popular Campaigns</h2>
            <span class="xs-separetor dashed-separetor fundpress-separetor"></span>
            <p>
              FundPress has built a platform focused on aiding entrepreneurs,
              startups, and companies raise capital from anyone.
            </p>
          </div>
          <!-- .xs-heading-title .fundpress-heading-title .xs-col-9 END -->
          <div class="xs-btn-wraper xs-padding-0 col-xl-3 col-md-3 d-flex-center-end">
            <a href="#" class="xs-btn round-btn navy-blue-btn">all Campaigns</a>
          </div>
          <!-- .xs-btn-wraper .xs-col-3 .d-flex-center-end END -->
        </div>
        <!-- .xs-section-heading .fundpress-section-heading .xs-spilit-container END -->
        <div class="row">
          <div class="col-lg-4" v-for="(item, idx) in items" :key="idx">
            <div class="xs-box-shadow fundpress-popular-item xs-bg-white">
              <div class="fundpress-item-header">
                <img :src="item.image" alt>
                <div class="xs-item-header-content">
                  <div class="xs-skill-bar">
                    <div class="xs-skill-track">
                      <p>
                        <span
                          class="number-percentage-count number-percentage"
                          data-value="90"
                          data-animation-duration="3500"
                        >0</span>%
                      </p>
                    </div>
                  </div>
                </div>
              </div>
              <!-- .xs-item-header .fundpress-item-header END -->
              <div class="fundpress-item-content xs-content-padding bg-color-white">
                <ul class="xs-simple-tag fundpress-simple-tag">
                  <li>
                    <a href>Technology</a>
                  </li>
                </ul>
                <a
                  href="#"
                  class="d-block color-navy-blue fundpress-post-title"
                >{{item.title}}</a>
                <ul class="xs-list-with-content fundpress-list-item-content">
                  <li>
                    ${{item.price}}
                    <span>Unit Price</span>
                  </li>
                  <li>
                    <span
                      class="number-percentage-count number-percentage"
                      data-value="90"
                      data-animation-duration="3500"
                    >0</span>%
                    <span>Ordered</span>
                  </li>
                  <li>
                    3
                    <span>Days to go</span>
                  </li>
                </ul>
                <span class="xs-separetor border-separetor xs-separetor-v2 fundpress-separetor"></span>
                <div class="row xs-margin-0">
                  <div class="full-round fundpress-avatar">
                    <img src="assets/images/avatar/avatar_1.jpg" alt>
                  </div>
                  <div class="xs-avatar-title">
                    <a href="#">
                      <span>By</span>Ema Watson
                    </a>
                  </div>
                </div>
              </div>
              <!-- .fundpress-item-content END -->
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- End popular campaigns -->
  </div>
</template>

<script>
// @ is an alias to /src

import Listing from "@/components/Listing.vue";
import { db } from "../main";

export default {
  name: "home",
  components: {
    Listing
  },
  css: {
    loaderOptions: {
      sass: {
        data: `
          @import "@/styles/style.scss";
        `
      }
    }
  },
  data() {
    return {
      items: []
    };
  },
  firestore() {
    return {
      items: db.collection("items")
    };
  }
};
</script>
