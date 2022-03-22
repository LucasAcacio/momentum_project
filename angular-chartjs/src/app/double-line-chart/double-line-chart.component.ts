import { HttpClient } from '@angular/common/http';
import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';
import * as Chart from 'chart.js';


export class RetornoMensaAcumulado {
  constructor(
    public data: string,
    public retorno: number
  ) { }
}

@Component({
  selector: 'app-double-line-chart',
  templateUrl: './double-line-chart.component.html',
  styleUrls: ['./double-line-chart.component.scss']
})

export class DoubleLineChartComponent implements AfterViewInit {
  @ViewChild('doubleLineCanvas') doubleLineCanvas: ElementRef;
  doubleLineChart: any;
  retornoMensalAcumuladoCDI: RetornoMensaAcumulado[];
  retornoMensalAcumuladoIBOVESPA: RetornoMensaAcumulado[];
  retornoMensalAcumuladoMomentum: RetornoMensaAcumulado[];

  constructor( private httpClient: HttpClient ) { }

  ngAfterViewInit(): void {
    this.getRetornoMensalAcumulado();
  }
  async getRetornoMensalAcumulado(){
    this.retornoMensalAcumuladoCDI = await this.httpClient.get<RetornoMensaAcumulado[]>('http://localhost:5000/api/retorno_mensal_acumulado_cdi').toPromise();
    this.retornoMensalAcumuladoIBOVESPA = await this.httpClient.get<RetornoMensaAcumulado[]>('http://localhost:5000/api/retorno_mensal_acumulado_ibovespa').toPromise();
    this.retornoMensalAcumuladoMomentum = await this.httpClient.get<RetornoMensaAcumulado[]>('http://localhost:5000/api/retorno_mensal_acumulado_momentum').toPromise();
    this.doubleLineChartMethod();
  }

  doubleLineChartMethod(): void {
    let dates = [];
    let retornosCDI = [];
    let retornosIBOVESPA = [];
    let retornosMomentum = [];

    this.retornoMensalAcumuladoCDI.forEach(element => {
      dates.push(element.data)
      retornosCDI.push(element.retorno)
    });

    this.retornoMensalAcumuladoIBOVESPA.forEach(element => {
      retornosIBOVESPA.push(element.retorno)
    })

    this.retornoMensalAcumuladoMomentum.forEach(element => {
      retornosMomentum.push(element.retorno)
    })


    this.doubleLineChart = new Chart(this.doubleLineCanvas.nativeElement, {
      type: 'line',
      data: {
        labels: dates,
        datasets: [
          {
            label: "CDI",
            data: retornosCDI,
            borderColor: "rgb(255,102,102)",
            fill: true,
            lineTension: 0.2,
            radius: 5
          },
          {
            label: "IBOVESPA",
            data: retornosIBOVESPA,
            borderColor: "rgb(102,178,255)",
            fill: true,
            lineTension: 0.2,
            radius: 5
          },
          {
            label: "Momentum",
            data: retornosMomentum,
            borderColor: "rgb(102,255,102)",
            fill: true,
            lineTension: 0.2,
            radius: 5
          }
        ]
      },

      options: {
        responsive: true,
        title: {
          display: true,
          position: "top",
          text: "Retorno ultimo ano",
          fontSize: 20,
          fontColor: "#000",
          fontWeight: "bold"
        },
        legend: {
          display: true,
          position: "bottom",
          labels: {
            fontColor: "#999",
            fontSize: 14
          }
        }
      }
    })
  }
}
