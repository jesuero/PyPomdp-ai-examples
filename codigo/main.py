# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:56:20 2019

@author: Jesus
"""
import math
import argparse
import os
import json
import multiprocessing
from pomdp_runner import PomdpRunner
from pomdp_runner_interactive import PomdpRunnerInteractive
from pomdp_runner_interactive_tag import PomdpRunnerInteractiveTag
from pomdp_runner_silenciosa import PomdpRunnerSilenciosa
from pomdp_runner_silenciosa_tag import PomdpRunnerSilenciosaTag
from pomdp_runner_benchmark import PomdpRunnerBenchmark
from pomdp_runner_benchmark_tag import PomdpRunnerBenchmarkTag
from util import RunnerParams

def eligeProblema():
    print("Problema a resolver:")
    print("Problema del tigre")
    print("Problema del tag")
    print("Problema de los anuncios")
    print("Problema del puente")
    
def tigre():
      print("Has seleccionado el problema del tigre")
      alg = input("Escribe el nombre del algoritmo por el cual quieres resolverlo (POMCP o PBVI): ")
      if alg == "POMCP":
          print("Vas a resolver el problema del tigre mediante el algoritmo POMCP")
          tigreSimulacionPomcp()
      if alg == "PBVI":    
           print("Vas a resolver el problema del tigre mediante el algoritmo PBVI")
           tigreSimulacionPbvi()
           
def tigreSimulacionPomcp():
    tipoSimulacion = input("Escribe si quieres simulación interactiva, silenciosa o benchmark: ")
    if tipoSimulacion == "interactiva":
        tigrePomcpInteractiva()
    if tipoSimulacion == "silenciosa":
        tigrePomcpSilenciosa()
    if tipoSimulacion == "benchmark":
        tigrePomcpBenchmark()
        
def tigrePomcpInteractiva():
    print("Has seleccionado ejecución interactiva con POMCP para el Problema del Tigre")
    
    params = RunnerParams("tiger.POMDP",None,"pomcp",float('inf'),10,False,False)
    
    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerInteractive(params)
        runner.run(**algo_params)
    
def tigrePomcpSilenciosa():
    print("Has seleccionado ejecución silenciosa con POMCP para el Problema del Tigre")
    
    params = RunnerParams("tiger.POMDP",None,"pomcp",float('inf'),30,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerSilenciosa(params)
        runner.run(**algo_params)
        
def tigrePomcpBenchmark():
    print("Has seleccionado ejecución benchmark con POMCP para el Problema del Tigre")
    pasos = 0
    recompensa = 0
    listaPasos = []
    listaRecompensas = []
    for i in range(30):
        params = RunnerParams("tiger.POMDP",None,"pomcp",float('inf'),30,False,False)

        with open(params.algo_config) as algo_config:
            algo_params = json.load(algo_config)
            runner = PomdpRunnerBenchmark(params)
            a = runner.run(**algo_params)
       
        pasos += a[0]
        recompensa += a[1]
        print('Resuelto en {} pasos'.format(a[0]))
        print('Recompensa: {}'.format(a[1]))
        listaPasos.append(a[0])
        listaRecompensas.append(a[1])
        
    mediaPasos = pasos/30
    mediaRecompensa = recompensa/30
    desviaciones = calculaDesviacionTipica(listaPasos,listaRecompensas,mediaPasos,mediaRecompensa)
    print('=========================================================================')
    print('Media de pasos: {}'.format(mediaPasos))
    print('Recompensa media: {}'.format(mediaRecompensa))
    print('Desviación típica pasos: {}'.format(desviaciones[0]))
    print('Desviación típica recompensas: {}'.format(desviaciones[1]))
        
def  tigreSimulacionPbvi():
    tipoSimulacionPbvi = input("Escribe si quieres simulación interactiva, silenciosa o benchmark: ")
    if tipoSimulacionPbvi == "interactiva":
        tigrePbviInteractiva()
    if tipoSimulacionPbvi == "silenciosa":
        tigrePbviSilenciosa()
    if tipoSimulacionPbvi == "benchmark":
        tigrePbviBenchmark()
        
def tigrePbviInteractiva():
    print("Has seleccionado ejecución interactiva con PBVI para el Problema del Tigre")
     
    params = RunnerParams("tiger.POMDP",None,"pbvi",float('inf'),10,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerInteractive(params)
        runner.run(**algo_params)
        
def tigrePbviSilenciosa():
    print("Has seleccionado ejecución silenciosa con PBVI para el Problema del Tigre")
    
    params = RunnerParams("tiger.POMDP",None,"pbvi",float('inf'),30,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerSilenciosa(params)
        runner.run(**algo_params)
        
def tigrePbviBenchmark():
    print("Has seleccionado ejecución benchmark con PBVI para el Problema del Tigre")
    pasos = 0
    recompensa = 0
    listaPasos = []
    listaRecompensas = []
    for i in range(30):
        params = RunnerParams("tiger.POMDP",None,"pbvi",float('inf'),30,False,False)

        with open(params.algo_config) as algo_config:
            algo_params = json.load(algo_config)
            runner = PomdpRunnerBenchmark(params)
            a = runner.run(**algo_params)
       
        pasos += a[0]
        recompensa += a[1]
        print('Resuelto en {} pasos'.format(a[0]))
        print('Recompensa: {}'.format(a[1]))
        listaPasos.append(a[0])
        listaRecompensas.append(a[1])
        
    mediaPasos = pasos/30
    mediaRecompensa = recompensa/30
    desviaciones = calculaDesviacionTipica(listaPasos,listaRecompensas,mediaPasos,mediaRecompensa)
    print('=========================================================================')
    print('Media de pasos: {}'.format(mediaPasos))
    print('Recompensa media: {}'.format(mediaRecompensa))
    print('Desviación típica pasos: {}'.format(desviaciones[0]))
    print('Desviación típica recompensas: {}'.format(desviaciones[1]))

def tag():
      print("Has seleccionado el problema del tag")
      alg = input("Escribe el nombre del algoritmo por el cual quieres resolverlo (POMCP o PBVI): ")
      if alg == "POMCP":
          print("Vas a resolver el problema del tag mediante el algoritmo POMCP")
          tagSimulacionPomcp()
      if alg == "PBVI":    
           print("Vas a resolver el problema del tag mediante el algoritmo PBVI")
           tagSimulacionPbvi()
           
def tagSimulacionPomcp():
    tipoSimulacion = input("Escribe si quieres simulación interactiva, silenciosa o benchmark: ")
    if tipoSimulacion == "interactiva":
        tagPomcpInteractiva()
    if tipoSimulacion == "silenciosa":
        tagPomcpSilenciosa()
    if tipoSimulacion == "benchmark":
        tagPomcpBenchmark()
        
def  tagSimulacionPbvi():
    tipoSimulacionPbvi = input("Escribe si quieres simulación interactiva, silenciosa o benchmark: ")
    if tipoSimulacionPbvi == "interactiva":
        tagPbviInteractiva()
    if tipoSimulacionPbvi == "silenciosa":
        tagPbviSilenciosa()
    if tipoSimulacionPbvi == "benchmark":
        tagPbviBenchmark()
        
def tagPomcpInteractiva():
    print("Has seleccionado ejecución interactiva con POMCP para el Problema del Tag")
    
    params = RunnerParams("tag.POMDP",None,"pomcp",float('inf'),10,False,False)
    
    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerInteractiveTag(params)
        runner.run(**algo_params)
    
def tagPomcpSilenciosa():
    print("Has seleccionado ejecución silenciosa con POMCP para el Problema del Tag")
    
    params = RunnerParams("tag.POMDP",None,"pomcp",float('inf'),500,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerSilenciosaTag(params)
        runner.run(**algo_params)
        
def tagPomcpBenchmark():
    print("Has seleccionado ejecución benchmark con POMCP para el Problema del Tag")
    pasos = 0
    recompensa = 0
    listaPasos = []
    listaRecompensas = []
    for i in range(30):
        params = RunnerParams("tag.POMDP",None,"pomcp",float('inf'),30,False,False)

        with open(params.algo_config) as algo_config:
            algo_params = json.load(algo_config)
            runner = PomdpRunnerBenchmarkTag(params)
            a = runner.run(**algo_params)
       
        pasos += a[0]
        recompensa += a[1]
        print('Resuelto en {} pasos'.format(a[0]))
        print('Recompensa: {}'.format(a[1]))
        listaPasos.append(a[0])
        listaRecompensas.append(a[1])
        
    mediaPasos = pasos/30
    mediaRecompensa = recompensa/30
    desviaciones = calculaDesviacionTipica(listaPasos,listaRecompensas,mediaPasos,mediaRecompensa)
    print('=========================================================================')
    print('Media de pasos: {}'.format(mediaPasos))
    print('Recompensa media: {}'.format(mediaRecompensa))
    print('Desviación típica pasos: {}'.format(desviaciones[0]))
    print('Desviación típica recompensas: {}'.format(desviaciones[1]))
    
def tagPbviInteractiva():
    print("Has seleccionado ejecución interactiva con PBVI para el Problema del Tag")
     
    params = RunnerParams("tag.POMDP",None,"pbvi",float('inf'),10,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerInteractiveTag(params)
        runner.run(**algo_params)
        
def tagPbviSilenciosa():
    print("Has seleccionado ejecución silenciosa con PBVI para el Problema del Tag")
    
    params = RunnerParams("tag.POMDP",None,"pbvi",float('inf'),500,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerSilenciosaTag(params)
        runner.run(**algo_params)
        
def tagPbviBenchmark():
    print("Has seleccionado ejecución benchmark con PBVI para el Problema del Tag")
    pasos = 0
    recompensa = 0
    listaPasos = []
    listaRecompensas = []
    for i in range(30):
        params = RunnerParams("tag.POMDP",None,"pbvi",float('inf'),30,False,False)

        with open(params.algo_config) as algo_config:
            algo_params = json.load(algo_config)
            runner = PomdpRunnerBenchmarkTag(params)
            a = runner.run(**algo_params)
       
        pasos += a[0]
        recompensa += a[1]
        print('Resuelto en {} pasos'.format(a[0]))
        print('Recompensa: {}'.format(a[1]))
        listaPasos.append(a[0])
        listaRecompensas.append(a[1])
        
    mediaPasos = pasos/30
    mediaRecompensa = recompensa/30
    desviaciones = calculaDesviacionTipica(listaPasos,listaRecompensas,mediaPasos,mediaRecompensa)
    print('=========================================================================')
    print('Media de pasos: {}'.format(mediaPasos))
    print('Recompensa media: {}'.format(mediaRecompensa))
    print('Desviación típica pasos: {}'.format(desviaciones[0]))
    print('Desviación típica recompensas: {}'.format(desviaciones[1]))
    
def anuncio():
      print("Has seleccionado el problema de los anuncios")
      alg = input("Escribe el nombre del algoritmo por el cual quieres resolverlo (POMCP o PBVI): ")
      if alg == "POMCP":
          print("Vas a resolver el problema de los anuncios mediante el algoritmo POMCP")
          anuncioSimulacionPomcp()
      if alg == "PBVI":    
           print("Vas a resolver el problema de los anuncios mediante el algoritmo PBVI")
           anuncioSimulacionPbvi()
           
def anuncioSimulacionPomcp():
    tipoSimulacion = input("Escribe si quieres simulación interactiva, silenciosa o benchmark: ")
    if tipoSimulacion == "interactiva":
        anuncioPomcpInteractiva()
    if tipoSimulacion == "silenciosa":
        anuncioPomcpSilenciosa()
    if tipoSimulacion == "benchmark":
        anuncioPomcpBenchmark()
        
def anuncioPomcpInteractiva():
    print("Has seleccionado ejecución interactiva con POMCP para el Problema de los anuncios")
    
    params = RunnerParams("anuncios.POMDP",None,"pomcp",float('inf'),10,False,False)
    
    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerInteractive(params)
        runner.run(**algo_params)
    
def anuncioPomcpSilenciosa():
    print("Has seleccionado ejecución silenciosa con POMCP para el Problema de los anuncios")
    
    params = RunnerParams("anuncios.POMDP",None,"pomcp",float('inf'),100,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerSilenciosa(params)
        runner.run(**algo_params)
        
def anuncioPomcpBenchmark():
    print("Has seleccionado ejecución benchmark con POMCP para el Problema de los anuncios")
    pasos = 0
    recompensa = 0
    listaPasos = []
    listaRecompensas = []
    for i in range(30):
        params = RunnerParams("anuncios.POMDP",None,"pomcp",float('inf'),30,False,False)

        with open(params.algo_config) as algo_config:
            algo_params = json.load(algo_config)
            runner = PomdpRunnerBenchmark(params)
            a = runner.run(**algo_params)
       
        pasos += a[0]
        recompensa += a[1]
        print('Resuelto en {} pasos'.format(a[0]))
        print('Recompensa: {}'.format(a[1]))
        listaPasos.append(a[0])
        listaRecompensas.append(a[1])
        
    mediaPasos = pasos/30
    mediaRecompensa = recompensa/30
    desviaciones = calculaDesviacionTipica(listaPasos,listaRecompensas,mediaPasos,mediaRecompensa)
    print('=========================================================================')
    print('Media de pasos: {}'.format(mediaPasos))
    print('Recompensa media: {}'.format(mediaRecompensa))
    print('Desviación típica pasos: {}'.format(desviaciones[0]))
    print('Desviación típica recompensas: {}'.format(desviaciones[1]))
        
def anuncioSimulacionPbvi():
    tipoSimulacionPbvi = input("Escribe si quieres simulación interactiva, silenciosa o benchmark: ")
    if tipoSimulacionPbvi == "interactiva":
        anuncioPbviInteractiva()
    if tipoSimulacionPbvi == "silenciosa":
        anuncioPbviSilenciosa()
    if tipoSimulacionPbvi == "benchmark":
        anuncioPbviBenchmark()
        
def anuncioPbviInteractiva():
    print("Has seleccionado ejecución interactiva con PBVI para el Problema de los anuncios")
     
    params = RunnerParams("anuncios.POMDP",None,"pbvi",float('inf'),10,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerInteractive(params)
        runner.run(**algo_params)
        
def anuncioPbviSilenciosa():
    print("Has seleccionado ejecución silenciosa con PBVI para el Problema de los anuncios")
    
    params = RunnerParams("anuncios.POMDP",None,"pbvi",float('inf'),100,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerSilenciosa(params)
        runner.run(**algo_params)
        
def anuncioPbviBenchmark():
    print("Has seleccionado ejecución benchmark con PBVI para el Problema de los anuncios")
    pasos = 0
    recompensa = 0
    listaPasos = []
    listaRecompensas = []
    for i in range(30):
        params = RunnerParams("anuncios.POMDP",None,"pbvi",float('inf'),30,False,False)

        with open(params.algo_config) as algo_config:
            algo_params = json.load(algo_config)
            runner = PomdpRunnerBenchmark(params)
            a = runner.run(**algo_params)
       
        pasos += a[0]
        recompensa += a[1]
        print('Resuelto en {} pasos'.format(a[0]))
        print('Recompensa: {}'.format(a[1]))
        listaPasos.append(a[0])
        listaRecompensas.append(a[1])
        
    mediaPasos = pasos/30
    mediaRecompensa = recompensa/30
    desviaciones = calculaDesviacionTipica(listaPasos,listaRecompensas,mediaPasos,mediaRecompensa)
    print('=========================================================================')    
    print('Media de pasos: {}'.format(mediaPasos))
    print('Recompensa media: {}'.format(mediaRecompensa))
    print('Desviación típica pasos: {}'.format(desviaciones[0]))
    print('Desviación típica recompensas: {}'.format(desviaciones[1]))
    
def puente():
      print("Has seleccionado el problema del puente")
      alg = input("Escribe el nombre del algoritmo por el cual quieres resolverlo (POMCP o PBVI): ")
      if alg == "POMCP":
          print("Vas a resolver el problema del puente mediante el algoritmo POMCP")
          puenteSimulacionPomcp()
      if alg == "PBVI":    
           print("Vas a resolver el problema del puente mediante el algoritmo PBVI")
           puenteSimulacionPbvi()
           
def puenteSimulacionPomcp():
    tipoSimulacion = input("Escribe si quieres simulación interactiva, silenciosa o benchmark: ")
    if tipoSimulacion == "interactiva":
        puentePomcpInteractiva()
    if tipoSimulacion == "silenciosa":
        puentePomcpSilenciosa()
    if tipoSimulacion == "benchmark":
        puentePomcpBenchmark()
        
def puentePomcpInteractiva():
    print("Has seleccionado ejecución interactiva con POMCP para el Problema del Puente")
    
    params = RunnerParams("puente.POMDP",None,"pomcp",float('inf'),10,False,False)
    
    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerInteractive(params)
        runner.run(**algo_params)
    
def puentePomcpSilenciosa():
    print("Has seleccionado ejecución silenciosa con POMCP para el Problema del Puente")
    
    params = RunnerParams("puente.POMDP",None,"pomcp",float('inf'),100,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerSilenciosa(params)
        runner.run(**algo_params)
        
def puentePomcpBenchmark():
    print("Has seleccionado ejecución benchmark con POMCP para el Problema del Puente")
    pasos = 0
    recompensa = 0
    listaPasos = []
    listaRecompensas = []
    for i in range(30):
        params = RunnerParams("puente.POMDP",None,"pomcp",float('inf'),30,False,False)

        with open(params.algo_config) as algo_config:
            algo_params = json.load(algo_config)
            runner = PomdpRunnerBenchmark(params)
            a = runner.run(**algo_params)
       
        pasos += a[0]
        recompensa += a[1]
        print('Resuelto en {} pasos'.format(a[0]))
        print('Recompensa: {}'.format(a[1]))
        listaPasos.append(a[0])
        listaRecompensas.append(a[1])
        
    mediaPasos = pasos/30
    mediaRecompensa = recompensa/30
    desviaciones = calculaDesviacionTipica(listaPasos,listaRecompensas,mediaPasos,mediaRecompensa)
    print('=========================================================================')   
    print('Media de pasos: {}'.format(mediaPasos))
    print('Recompensa media: {}'.format(mediaRecompensa))
    print('Desviación típica pasos: {}'.format(desviaciones[0]))
    print('Desviación típica recompensas: {}'.format(desviaciones[1]))
              
def  puenteSimulacionPbvi():
    tipoSimulacionPbvi = input("Escribe si quieres simulación interactiva, silenciosa o benchmark: ")
    if tipoSimulacionPbvi == "interactiva":
        puentePbviInteractiva()
    if tipoSimulacionPbvi == "silenciosa":
        puentePbviSilenciosa()
    if tipoSimulacionPbvi == "benchmark":
        puentePbviBenchmark()
        
def puentePbviInteractiva():
    print("Has seleccionado ejecución interactiva con PBVI para el Problema del Puente")
     
    params = RunnerParams("puente.POMDP",None,"pbvi",float('inf'),10,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerInteractive(params)
        runner.run(**algo_params)
        
def puentePbviSilenciosa():
    print("Has seleccionado ejecución silenciosa con PBVI para el Problema del Puente")
    
    params = RunnerParams("puente.POMDP",None,"pbvi",float('inf'),100,False,False)

    with open(params.algo_config) as algo_config:
        algo_params = json.load(algo_config)
        runner = PomdpRunnerSilenciosa(params)
        runner.run(**algo_params)
        
def puentePbviBenchmark():
    print("Has seleccionado ejecución benchmark con PBVI para el Problema del Puente")
    pasos = 0
    recompensa = 0
    listaPasos = []
    listaRecompensas = []
    for i in range(30):
        params = RunnerParams("puente.POMDP",None,"pbvi",float('inf'),30,False,False)

        with open(params.algo_config) as algo_config:
            algo_params = json.load(algo_config)
            runner = PomdpRunnerBenchmark(params)
            a = runner.run(**algo_params)
       
        pasos += a[0]
        recompensa += a[1]
        print('Resuelto en {} pasos'.format(a[0]))
        print('Recompensa: {}'.format(a[1]))
        listaPasos.append(a[0])
        listaRecompensas.append(a[1])
        
    mediaPasos = pasos/30
    mediaRecompensa = recompensa/30
    desviaciones = calculaDesviacionTipica(listaPasos,listaRecompensas,mediaPasos,mediaRecompensa)
    print('=========================================================================')    
    print('Media de pasos: {}'.format(mediaPasos))
    print('Recompensa media: {}'.format(mediaRecompensa))
    print('Desviación típica pasos: {}'.format(desviaciones[0]))
    print('Desviación típica recompensas: {}'.format(desviaciones[1]))
    
def calculaDesviacionTipica(listaPasos,listaRecompensas,mediaPasos,mediaRecompensa):
    sumatorioPasos = 0
    sumatorioRecompensa = 0
    for i in range(30):
        sumatorioPasos += pow(listaPasos[i]-mediaPasos,2)
        sumatorioRecompensa += pow(listaRecompensas[i]-mediaRecompensa,2)
    
    desviacionPasos = math.sqrt(sumatorioPasos/30)
    desviacionRecompensa = math.sqrt(sumatorioRecompensa/30)  
    return desviacionPasos,desviacionRecompensa
    
if __name__ == '__main__':
    eligeProblema()
    problema = input("Escribe el nombre del problema que quieres resolver: ")
    if problema == "Problema del tigre":
        tigre()
    if problema == "Problema del tag":
        tag()
    if problema == "Problema de los anuncios":
        anuncio()
    if problema == "Problema del puente":
        puente()