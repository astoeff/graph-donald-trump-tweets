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
          this.years_data = this.msg.split(/(\s+)/).filter((e) => e.trim().length > 1);
          console.log(this.years_data[0]);
          this.chartdata = {
            labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            datasets: [
              {
                label: 'Tweets count per year for 2014-2020',
                backgroundColor: [
                  'Red',
                  'Green',
                  'Salmon',
                  'Orange',
                  'MidnightBlue',
                  'Cyan',
                  'Brown',
                ],
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
