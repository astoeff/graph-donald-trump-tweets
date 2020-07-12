<script>
import { Bar } from 'vue-chartjs';
import axios from 'axios';

export default {
  extends: Bar,
  data: () => ({
    chartdata: null,
    msg: null,
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  }),
  methods: {
    filldata() {
      const path = 'http://localhost:5000/by-year';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          this.msg += '';
          this.years_data = this.msg.split(/(\s+)/).filter((e) => e.trim().length > 1);
          console.log(this.years_data[0]);
          this.chartdata = {
            labels: ['2014', '2015', '2016', '2017', '2018', '2019', '2020'],
            datasets: [
              {
                label: 'Tweets count per year for 2014-2020',
                backgroundColor: 'Darksalmon',
                data: [Number(this.years_data[0]), Number(this.years_data[1]),
                  Number(this.years_data[2]), Number(this.years_data[3]),
                  Number(this.years_data[4]),
                  Number(this.years_data[5]), Number(this.years_data[6])],
              },
            ],
          };
          this.renderChart(this.chartdata, this.options);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },

  mounted() {
    this.filldata();
  },
};

</script>
