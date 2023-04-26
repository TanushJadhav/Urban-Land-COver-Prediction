
import pickle
import streamlit as st
import base64

# loading the trained model
pickle_in = open('ulc_classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache_data()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(BrdIndx, Area, Round, Bright, Compact, ShpIndx, Mean_G, Mean_R,Mean_NIR,SD_G,SD_R,SD_NIR,LW,GLCM1,Rect,GLCM2,Dens,Assym,NDVI,BordLngth,GLCM3):   
    import pickle
    import streamlit as st
    pickle_in = open('ulc_classifier.pkl', 'rb') 
    classifier = pickle.load(pickle_in)
    # Making predictions 
    prediction = classifier.predict( 
        [[BrdIndx, Area, Round, Bright, Compact, ShpIndx, Mean_G, Mean_R, Mean_NIR,SD_G,SD_R,SD_NIR,LW,GLCM1,Rect,GLCM2,Dens,Assym,NDVI,BordLngth,GLCM3]])
     
    if prediction == 0:
        pred = 'grass'
    elif prediction == 1:
        pred = "building"
    elif prediction == 2:
        pred = "concrete"
    elif prediction == 3:
        pred = "tree"
    elif prediction == 4:
        pred = "shadow"
    elif prediction == 5:
        pred = "pool"
    elif prediction == 6:
        pred = "asphalt"
    elif prediction == 7:
        pred = "soil"
    else:
        pred = 'car'
    return pred
    
# this is the main function in which we define our webpage  
def main():

    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)

    set_background("DSC06721.JPG")
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:green;padding:13px"> 
    <h1 style ="color:yellow;text-align:center;">Urban Land Cover Prediction ML App</h1> 
    </div> 
    """
    
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    

    # following lines create boxes in which user can enter data required to make prediction 
    BrdIndx = st.number_input('Border Index')
    Area = st.number_input('Area') 
    Round = st.number_input("Round") 
    Bright = st.number_input("Bright")
    Compact = st.number_input("Compact")
    ShpIndx = st.number_input("ShpIndx")
    Mean_G =st.number_input("Mean_G")
    Mean_R = st.number_input("Mean_R")
    Mean_NIR = st.number_input("Mean_NIR")
    SD_G = st.number_input("SD_G")
    SD_R = st.number_input("SD_R")
    SD_NIR =st.number_input("SD_NIR")
    LW = st.number_input("LW")
    GLCM1 = st.number_input("GLCM1")
    Rect = st.number_input("Rect")
    GLCM2 = st.number_input("GLCM2")
    Dens = st.number_input("Dens")
    Assym = st.number_input("Assym")
    NDVI = st.number_input("NDVI")
    BordLngth = st.number_input("BordLngth")
    GLCM3 =st.number_input("GLCM3")
    result =""
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(BrdIndx, Area, Round, Bright, Compact, ShpIndx, Mean_G, Mean_R,Mean_NIR,SD_G,SD_R,SD_NIR,LW,GLCM1,Rect,GLCM2,Dens,Assym,NDVI,BordLngth,GLCM3)
        st.success('Your Predicted Land Cover is {}'.format(result))
        print(result)
    
if __name__=='__main__': 
    main()
