import streamlit as st
# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Đại Từ Điển Ngôn Ngữ Mạng", page_icon="📚", layout="wide")

# --- KHO DỮ LIỆU TỔNG HỢP SIÊU CẤP (GỘP TRỰC TIẾP) ---
# Chứa: Từ vựng, Phân loại, Ý nghĩa chi tiết và Link ảnh minh họa
slangs = [
    # --- NHÓM GEN Z (HOT TREND) ---
    {"word": "Chằm Zn", "cat": "Gen Z", "mean": "Trạng thái trầm cảm, mệt mỏi (Kẽm ký hiệu là Zn).", "img": "https://image.voh.com.vn/voh/Image/2021/04/08/cham-zn-la-gi-teencode-voh-4.jpg?t=o"},
    {"word": "Flex", "cat": "Gen Z", "mean": "Khoe khoang thành tích một cách tinh tế, khéo léo.", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5a7hAlXaR-fEjLEFTKxPA-HUqCSLDQQrmHQ&s"},
    {"word": "Ét ô ét", "cat": "Gen Z", "mean": "SOS - Cầu cứu hoặc dùng khi gặp tình huống cạn lời.", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUZ1jk51sCN8JUl3EqN68CNPCKFxojH2ToNw&s"},
    {"word": "Check var", "cat": "Xu hướng", "mean": "Kiểm tra, xác minh sự thật (mượn từ VAR trong bóng đá).", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZvSPE_ArXekBz-CKANzCK2rW_Nuf4yyCMKw&s"},
    {"word": "Xịt keo", "cat": "Gen Z", "mean": "Trạng thái đứng hình, sượng trân không nói nên lời.", "img": "https://image.voh.com.vn/voh/Image/2023/10/06/xit-keo-la-gi.jpg"},
    {"word": "Vô tri", "cat": "Gen Z", "mean": "Hành động ngớ ngẩn nhưng cực kỳ gây cười.", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2IOtwzgaQBRIVErnfRkn3Ze33ohm6_hdsOQ&s"},
    {"word": "Ngoan xinh yêu", "cat": "Xu hướng", "mean": "Cách cưng nựng người yêu hoặc trẻ con cực hot.", "img": "https://cdn-media.sforum.vn/storage/app/media/anhthem/hinh-nen-tinh-yeu-thumbnail.jpg"},
    {"word": "Elm", "cat": "Xu hướng", "mean": "Cách gọi 'Em' điệu đà từ trend Pam yêu ơi.", "img": "https://35express.org/wp-content/uploads/2025/08/elm-la-gi.png"},
    {"word": "Cứu dữ chưa", "cat": "Xu hướng", "mean": "Câu hỏi khi thấy ai đó gặp tình huống khó đỡ.", "img": "https://cdn2.fptshop.com.vn/unsafe/Uploads/images/tin-tuc/185857/Originals/meme-het-cuu%20(3).jpg"},
    {"word": "Over hợp", "cat": "Gen Z", "mean": "Rất phù hợp, cực kỳ ăn ý trong mọi chuyện.", "img": "https://toquoc.mediacdn.vn/280518851207290880/2023/7/6/35028309216632671674199676450268986420514845n-1688635937900549716538.jpeg"},
    {"word": "Thao túng tâm lý", "cat": "Gen Z", "mean": "Điều khiển suy nghĩ người khác theo ý mình.", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLgPwIxl8C0P6a6YfLUFp-o1AWIOgvwYYMsA&s"},
    {"word": "Kiếp nạn thứ 82", "cat": "Xu hướng", "mean": "Những rắc rối đen đủi ập đến bất ngờ.", "img": "https://image.voh.com.vn/voh/Image/2023/07/11/kiep-nan-thu-82-2.jpg?t=o&w=1600&q=85"},
    
    # --- NHÓM GEN ALPHA (MỚI NHẤT) ---
    {"word": "Skibidi", "cat": "Gen Alpha", "mean": "Kỳ quặc, xấu xa hoặc... cực đỉnh tùy ngữ cảnh.", "img": ""},
    {"word": "Sigma", "cat": "Gen Alpha", "mean": "Người ngầu, đơn độc, bản lĩnh và thành công.", "img": ""},
    {"word": "Mewing", "cat": "Gen Alpha", "mean": "Hành động ra hiệu im lặng để khoe xương hàm ngầu.", "img": ""},
    {"word": "Rizz", "cat": "Gen Alpha", "mean": "Khả năng quyến rũ, thu hút người khác cực mạnh.", "img": ""},
    {"word": "Gyatt", "cat": "Gen Alpha", "mean": "Thán từ khi thấy điều gì đó quá ấn tượng.", "img": ""},

    # --- NHÓM ĐỜI ĐẦU & VĂN HÓA MẠNG ---
    {"word": "Hết nước chấm", "cat": "Văn hóa mạng", "mean": "Tuyệt vời đến mức không còn gì để chê.", "img": "https://phongthe.edu.vn/upload/2025/08/meme-khinh-bi-10.webp"},
    {"word": "Cùi bắp", "cat": "Đời đầu", "mean": "Kém cỏi, lỗi thời, chất lượng thấp.", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmjXf6VA2GgqcM3SjzSc0Eh3yGx7AJr_TDyg&s"},
    {"word": "Gà mờ", "cat": "Đời đầu", "mean": "Người mới ngây ngô, chưa có kinh nghiệm.", "img": "https://kenh14cdn.com/203336854389633024/2020/11/27/anh-chup-man-hinh-2020-11-27-luc-194044-16064809920291906966124.png"},
    {"word": "Trà xanh", "cat": "Văn hóa mạng", "mean": "Kẻ thứ ba đóng vai ngây thơ phá hoại tình cảm.", "img": "https://img.vietcetera.com/uploads/images/21-jan-2021/2021021-chuvoinghia-tirnhsang-01-768x432.jpg"},
    {"word": "Cơm chó", "cat": "Văn hóa mạng", "mean": "Chứng kiến các cặp đôi thể hiện tình cảm quá mức.", "img": "https://cdn-media.sforum.vn/storage/app/media/duyentran/com-cho-la-gi-thumb.jpg"},
    {"word": "Sống ảo", "cat": "Văn hóa mạng", "mean": "Chăm chút mạng xã hội khác xa thực tế ngoài đời.", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4vXSwfsbhHkL19-p0MYJVoe-3KIjD39oXw&s"},
    {"word": "À lôi", "cat": "Xu hướng", "mean": "Trời ơi! (Tiếng Tày, cực hot từ rapper B Ray).", "img": "data:image/jpeg;base64,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"}
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









import streamlit as st

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Siêu Từ Điển Ngôn Ngữ Mạng", page_icon="🇻🇳", layout="wide")

# --- 2. KHO DỮ LIỆU KHỔNG LỒ (ĐÃ CẬP NHẬT LINK ẢNH THẬT 100%) ---
slangs = [
    {
        "word": "Flex", 
        "cat": "Gen Z", 
        "mean": "Khoe khoang thành tích cá nhân một cách khéo léo.", 
        "img": "https://image.thanhnien.vn"
    },
    {
        "word": "Chằm Zn", 
        "cat": "Gen Z", 
        "mean": "Trầm cảm, mệt mỏi (Zn là ký hiệu hóa học của Kẽm).", 
        "img": "https://img.vietnamnet.vn"
    },
    {
        "word": "Ét ô ét", 
        "cat": "Gen Z", 
        "mean": "Cách đọc SOS. Dùng khi gặp tình huống khẩn cấp hoặc khó đỡ.", 
        "img": "https://cdn.vjshop.vn"
    },
    {
        "word": "Xịt keo", 
        "cat": "Gen Z", 
        "mean": "Trạng thái đứng hình, câm nín vì quá sượng trân.", 
        "img": "https://cdn.tgdd.vn"
    },
    {
        "word": "Check var", 
        "cat": "Xu hướng", 
        "mean": "Kiểm tra, xác minh lại sự thật của một thông tin.", 
        "img": "https://static-images.vnncdn.net"
    },
    {
        "word": "Vô tri", 
        "cat": "Gen Z", 
        "mean": "Hành động ngớ ngẩn nhưng gây cười cực mạnh.", 
        "img": "https://cdn.tgdd.vn"
    },
    {
        "word": "À lôi", 
        "cat": "Xu hướng", 
        "mean": "Tiếng Tày nghĩa là 'Trời ơi'. Hot trend từ rapper B Ray.", 
        "img": "https://vtv1.mediacdn.vn"
    },
    {
        "word": "Ngoan xinh yêu", 
        "cat": "Xu hướng", 
        "mean": "Cách cưng nựng cực hot từ trend Pam yêu ơi.", 
        "img": "https://kenh14cdn.com"
    }
]

# --- 3. GIAO DIỆN CHÍNH ---
st.title("📚 SIÊU TỪ ĐIỂN NGÔN NGỮ MẠNG VIỆT NAM")
st.markdown("### Dự án liệt kê hơn 30+ thuật ngữ 'hot' nhất (Thuần Python)")

# Thanh tìm kiếm và lọc
c1, c2 = st.columns([3, 1])
with c1:
    search_q = st.text_input("🔍 Tra cứu từ lóng...", "").lower()
with c2:
    cat_list = ["Tất cả"] + sorted(list(set(i["cat"] for i in slangs)))
    selected_cat = st.selectbox("📂 Phân loại:", cat_list)

# Logic lọc dữ liệu
filtered = [i for i in slangs if search_q in i['word'].lower()]
if selected_cat != "Tất cả":
    filtered = [i for i in filtered if i['cat'] == selected_cat]

st.divider()

# --- 4. HIỂN THỊ DẠNG LƯỚI ---
if filtered:
    cols = st.columns(3) 
    for idx, item in enumerate(filtered):
        with cols[idx % 3]:
            with st.container(border=True):
                # Tiêu đề từ vựng
                st.subheader(f":red[{item['word']}]")
                st.caption(f"Nhóm: {item['cat']}")
                
                # Hiển thị ảnh (Sử dụng tham số để ảnh không bị lỗi kích thước)
                st.image(item['img'], use_container_width=True)
                
                # Ý nghĩa
                st.write(f"**Ý nghĩa:** {item['mean']}")
else:
    st.error("Không tìm thấy từ này trong bộ từ điển! 😅")

# --- 5. CHÂN TRANG ---
st.divider()
st.caption("© 2024 ICANTECH Project - Lập trình thuần Python với Streamlit")
