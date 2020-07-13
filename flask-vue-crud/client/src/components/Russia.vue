<script>
import { Pie } from 'vue-chartjs';
import axios from 'axios';

export default {
  extends: Pie,
  data: () => ({
    chartdata: null,
    msg: null,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      legend: {
        display: true,
      },
      title: {
        display: true,
        text: 'Tweets including "Russia" by day',
      },
    },
  }),
  methods: {
    filldata() {
      const path = 'http://localhost:5000/russia';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          this.msg += '';
          this.data_for_russia_per_day = this.msg.split(/(\s+)/).filter((e) => e.trim().length > 1);
          this.chartdata = {
            labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            datasets: [
              {
                backgroundColor: [
                  'Red',
                  'Green',
                  'Salmon',
                  'Orange',
                  'MidnightBlue',
                  'Cyan',
                  'Brown',
                ],
                data: [Number(this.data_for_russia_per_day[0]),
                  Number(this.data_for_russia_per_day[1]),
                  Number(this.data_for_russia_per_day[2]), Number(this.data_for_russia_per_day[3]),
                  Number(this.data_for_russia_per_day[4]), Number(this.data_for_russia_per_day[5]),
                  Number(this.data_for_russia_per_day[6])],
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
