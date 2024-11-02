import streamlit as st

def mostrar_pagina():
    st.markdown("<h3 style='text-align: center;'>Universidade de Santiago de Compostela</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Grao en Intelixencia Artificial</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Proxecto Integrador I</h4>", unsafe_allow_html=True)
    
    st.write("Este proyecto se encuadra dentro del caso de Uso \"Sistema de monitorización de eventos en los últimos tramos del Camino de Santiago\".")
    st.write("Se ha desarrollado esta aplicación web que agrupa todas las funcionalidades requeridas por el caso de uso planteado por la entidad colaboradora AMTEGA.")
