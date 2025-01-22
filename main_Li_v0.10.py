# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 12:38:29 2023

@author: Byungki Ryu @ KERI
"""

import webbrowser
import math
import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from PIL import Image
### bokeh version should be 2.4.3

path_data = "./data/"
path_figs = "./figs/"

# datafile_prefix = "Cu_and_Al_data_20230404_merged"
datafile_prefix = "Li_data_ver1p0_20250120"
sheet_name = 'Li_ver1.0'


def gradientbars(bars):
    grad = np.atleast_2d(np.linspace(0,1,256)).T
    ax = bars[0].axes
    lim = ax.get_xlim()+ax.get_ylim()
    for bar in bars:
        bar.set_zorder(1)
        bar.set_facecolor("none")
        x,y = bar.get_xy()
        w, h = bar.get_width(), bar.get_height()
        ax.imshow(grad, extent=[x,x+w,y,y+h], aspect="auto", zorder=0)
    ax.axis(lim)

def draw_graph(X, Y, alloy_title, energy_option1, energy_title, length_of_candidates):     
    
    col1, col2 = st.columns([4,1])
    with col1:            
        figsize=((len(X)/3+5),4)
        fig2, ax2 = plt.subplots(figsize=figsize)      
        ax2.set_title("{} of {}".format(energy_title,alloy_title) )
        
        bar = ax2.bar(X,Y)    
        gradientbars(bar)  
        
        ax2.set_axisbelow(True)    
        ax2.set_xlabel('Additoinal element')
        ax2.set_ylabel('{} [eV]'.format(energy_title))
         
        st.pyplot(fig2)
    with col2:   
        if (energy_option1 == 'Segregation'):    
            image_arrow= Image.open(path_figs+'./arrow_Segregation_energy.png')
        if (energy_option1 == 'Binding'):    
            image_arrow= Image.open(path_figs+'./arrow_Binding_energy.png')
        st.image(image_arrow)
        
    if( length_of_candidates>4):   
        col1, col2 = st.columns([4,1])
        with col1:
            XX = np.array(range(len(X)))*(2*np.pi/len(X))
            YY = np.array(Y)        
            XX2 = list(XX)+[2*np.pi]
            YY2 = list(YY)+[list(YY)[0]]
            
            YY2_min = min(YY2) - 0.15
            YY2_max = max(YY2) + 0.15
            
            # YY2_min = math.floor(min(YY2))
            # YY2_max = math.ceil(max(YY2))
            
            # YY2_min = math.floor(min(YY2))-0.5
            # YY2_max = math.ceil(max(YY2))+0.5
            # if (YY2_min>0 ):
            #     YY2_min = -0.1
            # if (YY2_max <0 ):
            #     YY2_max = 0.1              
            
            figsize=(4,4)
            # figsize=(30,3)
            fig3, ax3 = plt.subplots(subplot_kw={'projection': 'polar'},figsize=figsize)
            
            ax3.plot(XX2, YY2,zorder=20)
            ax3.scatter(XX2, YY2, zorder=30)
           
            ax3.set_rlim(YY2_min,YY2_max)
            theta = np.pi * np.arange(0, 2.01, 0.01)
            ax3.plot(theta,[0]*len(theta), color='black',zorder=10,  linewidth=0.5)
            
            if (energy_option1 == 'Segregation'):
                label1, label2 = 'Solute', 'Segregation'
                if (YY2_max >0):
                    ax3.fill_between(theta,0,YY2_max, color='blue', alpha=0.15, label=label1)
                if (YY2_min <0):
                    ax3.fill_between(theta,YY2_min,0, color='red', alpha=0.15, label=label2)
                
            if (energy_option1 == 'Binding'):
                label1, label2 = 'Attractive', 'Repulsive'
                if (YY2_max >0):
                    ax3.fill_between(theta,0,YY2_max, color='blue', alpha=0.15, label=label1)
                if (YY2_min <0):
                    ax3.fill_between(theta,YY2_min,0, color='red', alpha=0.15, label=label2)
            
            ax3.set_xticks(XX)
            ax3.set_xticklabels(X)
            
            ax3.set_theta_offset(np.pi/2)
            ax3.set_theta_direction(-1)
            ax3.set_rlabel_position(+135)  # Move radial labels away from plotted line
            
            ax3.grid(True,alpha=0.5)
            ax3.set_title("{} of {}".format(energy_title,alloy_title) )
            # ax3.legend(loc='right',fontsize=5)
            # ax3.legend(bbox_to_anchor=(1.14, 0.5), loc="center left")
            ax3.legend(bbox_to_anchor=(0.9, -0.1), loc="lower left")
            st.pyplot(fig3)  
        
        with col2:            
            if (energy_option1 == 'Segregation'):    
                image_arrow= Image.open(path_figs+'./arrow_Segregation_energy.png')
            if (energy_option1 == 'Binding'):    
                image_arrow= Image.open(path_figs+'./arrow_Binding_energy.png')
            st.image(image_arrow)
            # st.pyplot(fig3)  
            



######################################
###Template Start
st.set_page_config(
    page_title="Li_v1.0",  # 탭 제목
    page_icon="🌟",  # 파비콘 (이모지 사용 가능)
    # layout="wide",  # 레이아웃: "centered" 또는 "wide"
    initial_sidebar_state="expanded"  # 사이드바 초기 상태
)


# st.title('Alloy Design DB - v-Li-0.1.1')
st.title('Lithium Alloy Design DB (v0.10)')
# st.markdown('-- This is demo for lithium alloy design')
st.markdown('-- Data version: Li_ver1.0 from KIMS ' + '-- DB structure: v0.33 from BR')
# st.markdown('-- **:red[Lite vs Super mode]**')
    
    
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Database", "Introduction", "Achievement", "World-wide", "Acknowledgement"])

with tab1:        
   
        
    
    with st.sidebar:       

        st.markdown('Developed on KIMS(data)// Data version: Li_v1.0 // Last update: 2025-01-22.')
        st.markdown('**:red[Lite vs Super mode]**')
        options =['Lite','Super']
        data_mode = st.radio(
            'Select :red[Mode] for Alloy Design DB:',
            options=options,
            index=0
            )
        
        if (data_mode == 'Lite'):
            supercode = st.text_input('Code is not required', 'LITE mode activated') 
            
            dafafile_Lite = datafile_prefix+"_{}.xlsx".format(data_mode)                
            datafile = dafafile_Lite
            df_data  = pd.read_excel(path_data+datafile, sheet_name=sheet_name)
            st.write(":red[Lite] mode provide a :red[small] subset of the DB. :red[(Data size:]", len(df_data),":red[)]")
            
            # subhead_of_tab1 = ""
            # st.subheader('Data Mode :red[{}]'.format(data_mode))
        
        if (data_mode == 'Super'):
            # st.markdown(":red[Super] mode may provides :red[extended] data. With proper code, exact results will be shown.")
            supercode = st.text_input('Input :red[CODE] to activate SUPER mode:', '1234asdf!@#$')

            try:
                datafile_givencode = datafile_prefix+"_{}.xlsx".format(supercode)
                datafile = datafile_givencode
                df_data  = pd.read_excel(path_data + datafile, sheet_name=sheet_name)
                st.write("Code :blue[MATCHED]: supermode activated, with exact DFT results. :blue[(Data size:]", len(df_data),":red[)]")
                
                # st.subheader('Data Mode :blue[{}]'.format(data_mode))
                    
            except:
                ## error mode activated ##
                data_mode = 'Noise'
                supercode = data_mode
                datafile_givencode = datafile_prefix+"_{}.xlsx".format(supercode)   
                datafile = datafile_givencode
                df_data  = pd.read_excel(path_data + datafile, sheet_name=sheet_name)   
                st.write("Code :red[INVALID]: extended-mode activated, but with :red[noise]. :red[(Data size:]", len(df_data),":red[)]")
                
                
                
                # with st.expander("See data table"):        
                #     st.write("Data size:", len(df_data))
                #     st.write(df_data)
        
    st.subheader(':red[{}] mode activated'.format(data_mode))
    st.markdown(":red[Super] mode may provides :red[extended] data. With proper code, exact results will be shown. :red[See left Sidebar].")
    

    
    st.header(':blue[Choose alloy system (M-X-Y) and target energy]')
    df_raw = df_data.copy()

    atomic_name_list = ['None']+list( df_raw['alloy_name'].drop_duplicates())
    atomic_name_default = atomic_name_list.index(atomic_name_list[0])
    alloy_name = st.selectbox(
        'Select :blue[main element] of alloy:',
        atomic_name_list, index=atomic_name_default)
    
    energy_option1 = st.selectbox(
        'Select :blue[energy] type',
        ('None','Segregation','Binding'))
    
    if (energy_option1 == 'Binding'):
        energy_option2 = st.selectbox(
            'Which binding energy would you like to investigate?',
            ('(bulk)','(surface)'))        

    df_0 = df_raw[ df_raw.alloy_name == alloy_name]
    
    
    if (energy_option1 != 'None'):            
        df_energy = df_0[ df_0.Energy_name == energy_option1]        
        df_segregation  = df_0[ df_0.Energy_name == 'Segregation']
        df_binding      = df_0[ df_0.Energy_name == 'Binding']
        df_binding_bulk = df_0[ df_0.system == 'bulk']
        df_binding_surf = df_0[ df_0.system == 'surface']
        
        if (energy_option1 == 'Segregation'):
            df_energy = df_segregation
            energy_option2 = ""
        elif (energy_option2 == '(bulk)'):
            df_energy = df_binding_bulk
        elif (energy_option2 == '(surface)'):
            df_energy = df_binding_surf
        
        ######################################


        st.header(':blue[One Body Candidates in {}-alloy (1st additional element, X)]'.format(alloy_name))
        
        df_1 = df_energy[ df_energy.body ==1]
        body_name1s_list = df_1.body_name1.drop_duplicates()
        body_name1s_candidates = st.multiselect(
            'Select :blue[body number 1 (X)] candidates',
            body_name1s_list)
   
        length_of_candidates = len(body_name1s_candidates)
        if( length_of_candidates>0):
            df_1_list = []
            # df_1_list = ['Li','B','C']
            for body_name1_candidate in body_name1s_candidates:
                df_1_each = df_1[ df_1.body_name1 == body_name1_candidate]
                df_1_list.append(df_1_each)
            df_1_candidates = pd.concat(df_1_list)
            st.write(df_1_candidates)
    
            alloy_title = "{}-X (in eV)".format(alloy_name) 
            energy_title = "{} Energy{}".format(energy_option1, energy_option2)
            X = df_1_candidates.body_name1
            Y = df_1_candidates.Energy_value
            draw_graph(X,Y, alloy_title, energy_option1, energy_title, length_of_candidates)
        
        ######################################

        st.header(':blue[Two Body Candidates in {}-alloy (1st and 2nd additional elements, X & Y)]'.format(alloy_name))
        df_2 = df_energy[ df_energy.body ==2]
        
        body_name1s_list = ['None']+list(df_2.body_name1.drop_duplicates())
        body_name1 = st.selectbox(
            'Select one :blue[body number 1 (X)]',
            body_name1s_list)
   
        df_2on1 = df_2[ df_2.body_name1 == body_name1]
        # st.write(df_2on1)
        
        body_name2s_list = df_2on1.body_name2.drop_duplicates()
        body_name2s_candidates = st.multiselect(
            'Select :blue[body number 2 (Y)] candidates',
            body_name2s_list)    
       
            
        length_of_candidates = len(body_name2s_candidates)       
        if( length_of_candidates>0):
            df_2on1_list = []
            for body_name2_candidate in body_name2s_candidates:
                df_2on1_each = df_2on1[ df_2on1.body_name2 == body_name2_candidate]
                df_2on1_list.append(df_2on1_each)
            df_2on1_candidates = pd.concat(df_2on1_list)
            st.write(df_2on1_candidates)
        
            alloy_title = "{}-{}-Y (in eV)".format(alloy_name,body_name1) 
            energy_title = "{} Energy{}".format(energy_option1, energy_option2)        
            X = df_2on1_candidates.body_name2
            Y = df_2on1_candidates.Energy_value
            draw_graph(X,Y, alloy_title, energy_option1,energy_title, length_of_candidates)



with tab2:
    st.subheader(":blue[Atomic interaction in Alloy] by Bing Image Creater")
    col1, col2 = st.columns([3, 2])
    # if (1):
    with col1:
        file_image_aialloy='./alloy_bing_creater_60e6686d-066f-4761-8874-293114bb7401.jfif'
        image_aialloy= Image.open(path_figs+file_image_aialloy)
        st.image(image_aialloy)
    with col2:
        with st.expander("Drawn using text generated by ChatGPT3.5 under B Ryu"):
            st.markdown(":blue[Text for AI Image Drawing]. This illustration shows a ball and stick model of the atomic\
                         structure of an alloy, with nanoprecipitation distortion that is coherent\
                         with the strain field. The atoms are represented as blue spheres,\
                         with connecting bonds in white. The nanoprecipitates are shown as small blue clusters,\
                         with their distribution represented at the atomic level. \
                         The distortion caused by the nanoprecipitates is shown in blue, \
                         with a darker tone indicating a higher degree of distortion. \
                         The overall color tone of the illustration is blue, \
                         creating a cohesive and visually appealing aesthetic.")
    
    st.header(':blue[Theoretical background]')
    with st.expander("See explanation"):        
        st.subheader('Early-state kinetics analysis')
        st.markdown('Materials can be strengthened by introducing additional elements.\
                    The Alloy Design DB aims to provide element-wise interactions for \
                    a given metal matrix. We refer to the additional elements as bodies.\
                    At an early stage, as a solid-state kinetics, the solid solution\
                    state of one body and the interaction between solute atoms of two\
                    bodies are crucial. Note that, the early stage is not equilibrium,\
                    but non-equilibrium. It is important to consider the energy based\
                    on the atomic chemical potentials of one body, while the energy\
                    with respect to the ground state is important for determining\
                    the long-term equilibrium structure.')
        st.markdown('For the early stage kinetics, segregation and binding energies are introduced as below.')
        st.subheader('Segregation energy')
        st.latex('E_{seg}[D] := ( E^{surf} [D] - E^{bulk} [D] ) - ( E_0^{surf} - E_0^{bulk})')
        st.markdown('Postive: solute in bulk, negative: segregation at surface')
        st.subheader('Binding energy  ')
        st.latex('E_{bind}^{bulk}[A-B]  = (E^{bulk}[A] + E^{bulk}[B]) - (E^{bulk}[AB]+E^{bulk}_0) ')
        st.latex('E_{bind}^{surf}[A-B]  = (E^{surf}[A] + E^{surf}[B]) - (E^{surf}[AB]+E^{surf}_0) ')
        st.markdown('Postive: atrractive or agglomeratoin, negative:repulsive')
    
    st.header(':blue[Reference]')    
    with st.expander("See explanation"):
        #st.subheader('Reference')
        image_fig1 = Image.open(path_figs+'fig1.jpg')
        st.image(image_fig1,
                  # width=800,
                  caption ="Fig. 1. See Figure 1 in [1].\
                  Here the interaction is calculated following the above binding energy definition")
        image_fig2 = Image.open(path_figs+'fig2.jpg')
        st.image(image_fig2,
                  # width=800,
                  caption ="Fig. 2. See Figure 1 in [2].\
                  Here the interaction is calculated for short distance.\
                  Same concept, but different definition.")    
        st.markdown('[1] H. S. Shin, S. Z. Han, E.-A. Choi, J. H. Ahn, S. Kim, and J. Lee,\
                    Co and Ti Effect on Hot Workability of Phosphor Bronze,\
                    Journal of Alloys and Compounds 903, 163778 (2022): see Fig. 1.')
        st.markdown('[2] E.-A. Choi, S. Z. Han, J. H. Ahn, S. Semboshi, J. Lee, and S. H. Lim,\
                    Computational Screening of Efficient Additive Elements to\
                    Stabilize the Interface between Cu Matrix and Ni2Si Precipitates\
                    in Cu–Ni–Si Alloys,\
                    Journal of Japan Institute of Copper 60, 293 (2021): see Fig. 1.')
    
### Publications
with tab3:
    st.header(':blue[Papers]')
    # st.markdown('1. Choi, Eun-Ae, Sang Jin Lee, Jee Hyuk Ahn, Seunghoe Choe, Kyu Hwan Lee, \
    #              Sung Hwan Lim, Yoon Suk Choi, and Seung Zeon Han. \
    #              “Enhancement of Strength and Electrical Conductivity for Hypo-Eutectic \
    #              Cu-12Ag Alloy.” \
    #              Journal of Alloys and Compounds 931 (January 10, 2023): 167506. \
    #              https://doi.org/10.1016/j.jallcom.2022.167506.')
    # st.markdown('2. Goto, Masahiro, Takaei Yamamoto, Eun-Ae Choi, Sangshik Kim,\
    #              Ren Hirano, Sung Hwan Lim, Jee-Hyuk Ahn, Jehyun Lee, and Seung Zeon Han.\
    #              “Physical Background of Significant Increase in Mechanical Properties and\
    #              Fatigue Strength of Groove-Rolled Cu-Ni-Si Alloy with Discontinuous Precipitates.”\
    #              Journal of Alloys and Compounds 947 (June 25, 2023): 169569.\
    #              https://doi.org/10.1016/j.jallcom.2023.169569.')
    # st.markdown('3. Ryu, Byungki, Jaywan Chung, Masaya Kumagai, Tomoya Mato, \
    #             Yuki Ando, Sakiko Gunji, Atsumi Tanaka, et al. \
    #             “Best Thermoelectric Efficiency of Ever-Explored Materials.” \
    #             IScience, March 27, 2023, 106494. https://doi.org/10.1016/j.isci.2023.106494.')
    # st.markdown('(Item Format: Chicago Manual of Style 17th edition (full note))')
    
    # st.header(':blue[Patents]')
    
    # st.header(':blue[Presentations]')    
    # st.markdown('1. Ryu, Byungki, Eun-Ae Choi, Sungjin Park, Seung Zeon Han, SuDong Park, and Jaywan Chung. “Prediction of Intrinsic and Extrinsic Interface Formation Energy Using a Universal Inter-Atomic Potential Based on Graph Neural Networks with Three-Body Interactions.” Oral presented at the 2022 Korean Physical Society (KPS) Fall Meeting, BEXCO, Busan, Korea, October 19, 2022.')
    # st.markdown('(Item Format: Chicago Manual of Style 17th edition (full note))')


with tab4:
    st.header(':blue[International]')
    # st.subheader('Test')
    # st.subheader('German Aerospace Center')
    st.subheader('Satoshi SEMBOSHI, Prof.')
    # st.markdown('Tohoku Univeristy')
     
#     st.header(':blue[Domestic (Korean)]')
    
#     st.subheader('한승우 교수님 (HAN Seungwu, Prof.)')
#     st.markdown('서울대학교 재료공학부')
#     st.markdown('Seoul National Univeristy (SNU))')
    
#     st.subheader('설재복 교수님 (SEOL Jae Bok, Prof.)')
#     st.markdown('경상국립대 나노신소재공학부 금속재료전공')
#     st.markdown('Gyeongsang National University (GNU)')

     
with tab5:
    st.header(':blue[Contribution]')

    st.subheader('최은애 박사 (한국재료연구원)')
    st.markdown('Dr. CHOI Eun-Ae @ Korea Institute of Materials Science (KIMS)')
    st.markdown('Theory and calculation method. Data from first-principles calculations. ')
    st.markdown(':red[Data generation from DFT]')

    st.subheader('류병기 박사 (한국전기연구원)')
    st.markdown('Dr. RYU Byungki @ Korea Electrotechnology Research Institute (KERI). Co-PI')
    st.markdown('Physics, Defects and interface, Computational Science. Data. Thermoelectrics. Alloys')
    st.markdown(':red[Database developer]')

    st.subheader('한승전 박사 (한국재료연구원)')
    st.markdown('Dr. HAN Seungzeon @ Korea Institute of Materials Science (KIMS). Principal Investigator (PI)')
    st.markdown('Metallurgist. Cu alloys')
    st.markdown(':red[Database parameters]')
    # link1 = '[Link for Online Thermoelectric Simulator](https://tes.keri.re.kr/)'
    # link2 = '[Link for Website](https://sites.google.com/view/tesimulator/)'
    # link3 = '[Link for Google Scholar](https://scholar.google.com/citations?user=fldxgiEAAAAJ&hl=ko)'
    # st.markdown(link1, unsafe_allow_html=True)
    # st.markdown(link2, unsafe_allow_html=True)
    # st.markdown(link3, unsafe_allow_html=True)

    # st.subheader('정재환 박사 (한국전기연구원)')
    # st.markdown('Dr. CHUNG Jaywan @ Korea Electrotechnology Research Institute (KERI)')
    # st.markdown('Database developer. Algorithm developer. Partial differential equation of heat diffusion. Alloy Machine Learning.')
        
    # st.header(':blue[Acknowledgement]')
    # st.markdown('This work is supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT).')
    # st.markdown('Project code  : :blue[NRF-2022M3C1C8093916]')
    # st.markdown('Project title : Strengthening by stable **:blue[heterogeneous phases]** in metal')
    # st.markdown('Project period: 2022-Sept to 2027 Dec.')

    # image_nanse= Image.open(path_figs+'./ci_kimskeri.png')
    # st.image(image_nanse)
    