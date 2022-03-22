import { HttpClient } from '@angular/common/http';
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';
import { Chart } from 'chart.js';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTable } from '@angular/material/table';
import { CarteiraDataSource, CarteiraItem } from '../pie-chart/carteira-datasource'
import { CDK_CONNECTED_OVERLAY_SCROLL_STRATEGY_PROVIDER_FACTORY } from '@angular/cdk/overlay/overlay-directives';

@Component({
  selector: 'app-pie-chart',
  templateUrl: './pie-chart.component.html',
  styleUrls: ['./pie-chart.component.scss']
})

export class PieChartComponent implements AfterViewInit {

  @ViewChild('pieCanvas') private pieCanvas: ElementRef;
  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatTable) table!: MatTable<CarteiraItem>;
  dataSource: CarteiraDataSource;

  /** Columns displayed in the table. Columns IDs can be added, removed, or reordered. */
  displayedColumns = ['codigo','retorno'];

  pieChart: any;
  retornoMensalMomentum: CarteiraItem[];

  constructor(
    private httpClient: HttpClient
  ) { }

  ngAfterViewInit() {
    this.getRetornoMensalMomentum(null);
  }

  onChangeEvent(event) {
    let thisYear = event.value.getFullYear()
    let thisMonth = event.value.getMonth() + 1
    let currentDate = `${thisYear}-${thisMonth}-1`
    this.getRetornoMensalMomentum(currentDate);
  }

  async getRetornoMensalMomentum(myDate){
    let url = 'http://localhost:5000/api/retorno_mensal_momentum_list'

    if (myDate != null) {
      url = `http://localhost:5000/api/retorno_mensal_momentum_list?start_date=${myDate}`
    } 

    this.retornoMensalMomentum = await this.httpClient.get<CarteiraItem[]>(url).toPromise();
    this.dataSource = new CarteiraDataSource(this.retornoMensalMomentum);
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
    this.table.dataSource = this.dataSource;
    this.pieChartBrowser();
  }

  pieChartBrowser() {
    let labels = []
    let colors = ['#fff100','#ff8c00','#e81123','#ec008c','#68217a','#00188f','#00bcf2','#00b294','#009e49','#bad80a']
    let datas = []

    this.retornoMensalMomentum.forEach(element => {
      labels.push(element.codigo)
      datas.push(element.retorno)
    })

    this.pieChart = new Chart(this.pieCanvas.nativeElement, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          backgroundColor: colors,
          data: datas,
        }]
      },
      options: {
        legend:{
          display: true,
          position: 'left'
        }
      }
    });
  }

}
