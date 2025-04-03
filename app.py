import streamlit as st
from model_operation import load_model, preprocess_input, predict_loan_approval
from user_interface import user_input, add_footer, add_social_media_links
from css_loader import load_css

st.set_page_config(page_title="ML Loan-Solutions Elite", page_icon="💸", layout="wide")
st.title("💸 ML Loan-solutions Elite")

load_css("style.css")

def main():

    model, scaler, vectorizer = load_model()
    
    if model is None or scaler is None or vectorizer is None:
        st.error("Failed to load the model, scaler, or vectorizer. Please check the logs.")
        return
    
    input_data = user_input()
    
    if st.button("Predict Loan Approval"):
        try:

            processed_input = preprocess_input(input_data, scaler, vectorizer)
            
            prediction = predict_loan_approval(model, processed_input)
            
            if prediction == 1:
                st.success(f"🎉 Congratulations! Your loan has been approved based on the following factors:\n"
                            f"- **Income**: Sufficient to support the loan.\n"
                            f"- **Credit Score**: Excellent, demonstrating strong financial reliability.\n"
                            f"- **DTI Score**: Healthy debt-to-income ratio.\n"
                            f"- **Employment Status**: Stable, adding to your financial security.\n"
                            f"We're excited to support your financial goals with a **loan approval**. "
                            f"Confident in your ability to manage it, we look forward to seeing you succeed!")
                st.balloons()
            else:
                st.error(f"❌ Sorry, your loan application has been rejected due to the following factors:\n"
                        f"- **Credit Score**: Below the required threshold.\n"
                        f"- **DTI Score**: High, suggesting significant existing debt.\n"
                        f"- **Employment Status**: Unstable, raising concerns about repayment.\n"
                        f"- **Loan Amount**: Requested amount exceeds your current financial capacity.\n"
                        f"We encourage you to improve these areas and reapply in the future. Best of luck!")


        except Exception as e:
            st.error(
                    f"🤔I think you had forgotten to enter your additional details. \n"
                    f"Please enter a valid reason to get your loan proposal accepted.\n"
                    f"❌An error occurred during prediction: {e}")

    add_footer()
    add_social_media_links()


if __name__ == "__main__":
    main()