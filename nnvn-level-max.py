import streamlit as st

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Đại Từ Điển Ngôn Ngữ Mạng", page_icon="📚", layout="wide")

# --- KHO DỮ LIỆU TỔNG HỢP SIÊU CẤP (GỘP TRỰC TIẾP) ---
# Chứa: Từ vựng, Phân loại, Ý nghĩa chi tiết và Link ảnh minh họa
slangs = [
    # --- NHÓM GEN Z (HOT TREND) ---
    {"word": "Chằm Zn", "cat": "Gen Z", "mean": "Trạng thái trầm cảm, mệt mỏi (Kẽm ký hiệu là Zn).", "img": "https://i.postimg.cc"},
    {"word": "Flex", "cat": "Gen Z", "mean": "Khoe khoang thành tích một cách tinh tế, khéo léo.", "img": "https://i.postimg.cc"},
    {"word": "Ét ô ét", "cat": "Gen Z", "mean": "SOS - Cầu cứu hoặc dùng khi gặp tình huống cạn lời.", "img": "https://i.postimg.cc"},
    {"word": "Check var", "cat": "Xu hướng", "mean": "Kiểm tra, xác minh sự thật (mượn từ VAR trong bóng đá).", "img": "https://via.placeholder.com"},
    {"word": "Xịt keo", "cat": "Gen Z", "mean": "Trạng thái đứng hình, sượng trân không nói nên lời.", "img": "https://via.placeholder.com"},
    {"word": "Vô tri", "cat": "Gen Z", "mean": "Hành động ngớ ngẩn nhưng cực kỳ gây cười.", "img": "https://via.placeholder.com"},
    {"word": "Ngoan xinh yêu", "cat": "Xu hướng", "mean": "Cách cưng nựng người yêu hoặc trẻ con cực hot.", "img": "https://via.placeholder.com"},
    {"word": "Elm", "cat": "Xu hướng", "mean": "Cách gọi 'Em' điệu đà từ trend Pam yêu ơi.", "img": "https://via.placeholder.com"},
    {"word": "Cứu dữ chưa", "cat": "Xu hướng", "mean": "Câu hỏi khi thấy ai đó gặp tình huống khó đỡ.", "img": "https://via.placeholder.com"},
    {"word": "Over hợp", "cat": "Gen Z", "mean": "Rất phù hợp, cực kỳ ăn ý trong mọi chuyện.", "img": "https://via.placeholder.com"},
    {"word": "Thao túng tâm lý", "cat": "Gen Z", "mean": "Điều khiển suy nghĩ người khác theo ý mình.", "img": "https://via.placeholder.com"},
    {"word": "Kiếp nạn thứ 82", "cat": "Xu hướng", "mean": "Những rắc rối đen đủi ập đến bất ngờ.", "img": "https://via.placeholder.com"},
    
    # --- NHÓM GEN ALPHA (MỚI NHẤT) ---
    {"word": "Skibidi", "cat": "Gen Alpha", "mean": "Kỳ quặc, xấu xa hoặc... cực đỉnh tùy ngữ cảnh.", "img": "https://via.placeholder.com"},
    {"word": "Sigma", "cat": "Gen Alpha", "mean": "Người ngầu, đơn độc, bản lĩnh và thành công.", "img": "https://via.placeholder.com"},
    {"word": "Mewing", "cat": "Gen Alpha", "mean": "Hành động ra hiệu im lặng để khoe xương hàm ngầu.", "img": "https://via.placeholder.com"},
    {"word": "Rizz", "cat": "Gen Alpha", "mean": "Khả năng quyến rũ, thu hút người khác cực mạnh.", "img": "https://via.placeholder.com"},
    {"word": "Gyatt", "cat": "Gen Alpha", "mean": "Thán từ khi thấy điều gì đó quá ấn tượng.", "img": "https://via.placeholder.com"},

    # --- NHÓM ĐỜI ĐẦU & VĂN HÓA MẠNG ---
    {"word": "Hết nước chấm", "cat": "Văn hóa mạng", "mean": "Tuyệt vời đến mức không còn gì để chê.", "img": "https://via.placeholder.com"},
    {"word": "Cùi bắp", "cat": "Đời đầu", "mean": "Kém cỏi, lỗi thời, chất lượng thấp.", "img": "https://via.placeholder.com"},
    {"word": "Gà mờ", "cat": "Đời đầu", "mean": "Người mới ngây ngô, chưa có kinh nghiệm.", "img": "https://via.placeholder.com"},
    {"word": "Trà xanh", "cat": "Văn hóa mạng", "mean": "Kẻ thứ ba đóng vai ngây thơ phá hoại tình cảm.", "img": "https://via.placeholder.com"},
    {"word": "Cơm chó", "cat": "Văn hóa mạng", "mean": "Chứng kiến các cặp đôi thể hiện tình cảm quá mức.", "img": "https://via.placeholder.com"},
    {"word": "Sống ảo", "cat": "Văn hóa mạng", "mean": "Chăm chút mạng xã hội khác xa thực tế ngoài đời.", "img": "https://via.placeholder.com"},
    {"word": "À lôi", "cat": "Xu hướng", "mean": "Trời ơi! (Tiếng Tày, cực hot từ rapper B Ray).", "img": "https://via.placeholder.com"}
]

# --- GIAO DIỆN CHÍNH ---
st.title("📚 ĐẠI TỪ ĐIỂN NGÔN NGỮ MẠNG VIỆT NAM")
st.write(f"Đang lưu trữ **{len(slangs)}** thuật ngữ mạng xã hội phổ biến.")

# Tìm kiếm & Lọc
col_search, col_filter = st.columns([2, 1])
with col_search:
    search_q = st.text_input("🔍 Tra cứu nhanh (nhập tên từ để tìm)...", "").lower()
with col_filter:
    cat_list = ["Tất cả"] + sorted(list(set(i["cat"] for i in slangs)))
    selected_cat = st.selectbox("📂 Phân loại thế hệ:", cat_list)

# Logic xử lý dữ liệu
filtered = [i for i in slangs if search_q in i['word'].lower()]
if selected_cat != "Tất cả":
    filtered = [i for i in filtered if i['cat'] == selected_cat]

st.divider()

# Hiển thị kết quả dạng Lưới (Grid)
if filtered:
    # Chia trang web thành 3 cột để xếp các thẻ từ vựng
    cols = st.columns(3)
    for index, item in enumerate(filtered):
        with cols[index % 3]:
            # Tạo khối hiển thị cho mỗi từ
            with st.container(border=True):
                st.subheader(f":red[{item['word']}]")
                st.caption(f"Nhóm: {item['cat']}")
                
                # Nút bấm mở rộng thông tin (Hình ảnh ẩn bên trong)
                with st.expander("👁️ Xem chi tiết & Ảnh"):
                    st.image(item['img'], use_container_width=True, caption=f"Minh họa cho: {item['word']}")
                    st.write(f"**Ý nghĩa:** {item['mean']}")
else:
    st.error("Không tìm thấy từ này. Hãy thử từ khác hoặc đóng góp cho mình nhé! 😅")

# --- CHÂN TRANG ---
st.divider()
st.info("💡 Mẹo: Bấm vào mục 'Xem chi tiết' ở mỗi thẻ để xem hình ảnh minh họa tương ứng.")
st.caption("Dự án ICANTECH - Lập trình thuần Python 100% với Streamlit")
