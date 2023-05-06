<template>
  <li class="d-flex justify-content-bw order-item">
    <div class="d-flex">
      <img class="menu-img" :src="order.menu.image" alt="" />
      <div class="d-flex flex-column">
        <p>{{ order.menu.title }}</p>
        <p>사이즈: {{ order.size.name }}</p>
      </div>
    </div>
    <div>가격: {{ totalPrice }}원</div>
  </li>
</template>

<script>
export default {
  name: "OrderListItem",
  props: {
    order: Object,
  },
  computed: {
    totalPrice() {
      return this.order.menu.price + this.order.size.price;
    },
  },
};
</script>

<style>
.order-item {
  padding: 10px;
}

.flex-column {
  flex-direction: column;
}
</style>