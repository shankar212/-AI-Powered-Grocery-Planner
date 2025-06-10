import streamlit as st
from gemini_planner import generate_meal_plan
from kroger_api import get_product_matches
from utils import build_shopping_list, calculate_total_cost
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import os

st.set_page_config(page_title="AI Grocery Planner", layout="wide")
st.title("\U0001F9E0 AI-Powered Grocery Planner")

with st.sidebar:
    st.header("User Preferences")
    diet = st.selectbox("Dietary Preference", ["Vegetarian", "Vegan", "Keto", "Diabetic", "None"])
    budget = st.number_input("Budget ($)", min_value=10, max_value=300, value=70)
    household = st.slider("Household Size", 1, 8, 2)
    include_oos = st.checkbox("Include Out-of-Stock Items", value=True)

    if st.button("Generate Meal Plan"):
        with st.spinner("Generating plan..."):
            plan = generate_meal_plan(diet, household, budget)
            st.session_state["plan"] = plan

if "plan" in st.session_state:
    st.subheader("\U0001F4C5 7-Day Meal Plan")
    for day in st.session_state.plan:
        st.markdown(f"**{day['day']}**")
        st.markdown(", ".join(day["meals"]))

    st.divider()
    st.subheader("\U0001F6D2 Smart Shopping List")

    ingredients = [ingredient for day in st.session_state.plan for meal in day["ingredients"] for ingredient in meal]
    product_matches = get_product_matches(ingredients)

    shopping_list = build_shopping_list(product_matches, include_out_of_stock=include_oos)
    total_cost = calculate_total_cost(shopping_list, only_in_stock=not include_oos)

    for item in shopping_list:
        status = "In stock" if item["in_stock"] else "Out of stock"
        st.write(f"{item['name']} — ${item['price']} ({status})")

    st.markdown(f"### \U0001F4B0 Total Cost: ${round(total_cost, 2)}")

    if total_cost > budget:
        st.warning("You're over budget. Consider reviewing substitutions or excluding out-of-stock items.")

    if st.button("Export List to PDF"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
            c = canvas.Canvas(tmpfile.name, pagesize=letter)
            width, height = letter
            y = height - 40

            c.setFont("Helvetica-Bold", 16)
            c.drawString(40, y, "🧾 Grocery Shopping List")
            y -= 30

            c.setFont("Helvetica", 12)
            for item in shopping_list:
                if y < 50:
                    c.showPage()
                    y = height - 40
                line = f"{item['name']} — ${item['price']} ({'In stock' if item['in_stock'] else 'Out of stock'})"
                c.drawString(40, y, line)
                y -= 20

            c.setFont("Helvetica-Bold", 14)
            c.drawString(40, y - 10, f"Total Cost: ${round(total_cost, 2)}")
            c.save()

            st.success("✅ PDF generated!")
            with open(tmpfile.name, "rb") as f:
                st.download_button("📥 Download PDF", f, file_name="shopping_list.pdf", mime="application/pdf")

        os.remove(tmpfile.name)
